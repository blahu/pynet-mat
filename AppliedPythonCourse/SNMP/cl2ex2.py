#!/usr/bin/env python
# Class 2
# Exercise 1
# Author mblaszczyk
'''
2. Using SNMPv3 create two SVG image files.  The first image file should graph
input and output octets on interface FA4 on pynet-rtr1 every five minutes for
an hour.  Use the pygal library to create the SVG graph file.  

The second SVG graph file should be the same as the first except graph unicast
packets received and transmitted.

The relevant OIDs are as follows:

    ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5')
    ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5')
    ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5')
    ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5'),
    ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5')
'''

import sys
import pygal
from time import sleep
from snmp_helper import snmp_get_oid,snmp_get_oid_v3,snmp_extract

from ROUTERS import ROUTERS
from OIDS import OIDS

def get_snmp_data (router_data, oid):

    if router_data ['snmp_v'] < 3:

        a_device = ( 
                router_data['IP'], 
                router_data['SNMP Community'], 
                router_data['SNMP Port'], 
        )

        snmp_data = snmp_get_oid ( a_device, oid)

        if snmp_data:
            return snmp_extract (snmp_data)

    if router_data ['snmp_v'] == 3:
        a_device = ( 
                router_data['IP'], 
                router_data['SNMP Port'], 
        )
        snmp_user = router_data ['snmp_user']

        snmp_data = snmp_get_oid_v3 ( a_device, snmp_user, oid)

        if snmp_data:
            return snmp_extract (snmp_data)
    
            
    return None


def rrd_add ( a_list, new, max_size=60):
    '''
    This function adds new to a_list.
    If list is longer than max_size,
    we pop old value and push a new one.
    '''
    
    # some senity checking
    if type(a_list) is not list:
        return None
    #ENDOF if type(...

    if len(a_list) >= max_size:
        a_list = a_list [1:]

    a_list.append(new)

    return (a_list)
#ENDOF def rrd_add


def get_iface_graph ( fn, title, in_list, in_title, out_list, out_title, times):
    '''
    Creates a graph using pygal in svg format
    Input/Output line graph in time.
    '''


    # Create a Chart of type Line
    line_chart = pygal.Line()

    # Title
    line_chart.title = title

    # X-axis labels (samples were every five minutes)
    line_chart.x_labels = times

    # Add each one of the above lists into the graph as a line with corresponding title
    line_chart.add(in_title,  in_list)
    line_chart.add(out_title, out_list)

    # Create an output image file from this
    line_chart.render_to_file(fn)
    return True

#ENDOF: def get_iface_graph ( fn, title, in_list, in_title, out_list, out_title, times)


def main():

    for router, router_data in ROUTERS.items():
        if sys.argv[1] in router:

            print
            print router
            idx = '.{}'.format(router_data['ifIndex'])

            # get current time
            from time import strftime
            curr_time = strftime('%Y-%m-%d %H:%M:%S')
            print 'Current Time={}'.format(curr_time)

            # get snmp ifDescr.IfIndex==1
            if_descr = get_snmp_data ( router_data, OIDS['ifDescr'] + idx)
            if if_descr:
                print 'ifDescr={}'.format(if_descr)

            # Loop for 60 minutes
            in_list = []
            out_list = []
            times = []

            max_size = 10
            seconds = 10
            for j in range(max_size):
                print 'j={}'.format(j)
                
                # for x-labels
                times.append('{}s'.format(j*seconds))

                # get snmp ifInOctets.IfIndex==1
                if_oct_in = get_snmp_data ( router_data, OIDS['ifInOctets'] + idx)
                if if_oct_in:
                    print 'ifInOctets={}'.format(if_oct_in)

                in_list = rrd_add (in_list, int(if_oct_in), max_size)

                # get snmp ifOutOctets.IfIndex==1
                if_oct_out = get_snmp_data ( router_data, OIDS['ifOutOctets'] + idx)
                if if_oct_out:
                    print 'ifOutOctets={}'.format(if_oct_out)

                out_list = rrd_add (out_list, int(if_oct_out), max_size)

                # sleep seconds
                sleep(seconds)
            #EMDOF:for i in (range(10):
 
            get_iface_graph ( '{}_{}.svg'.format(router,if_descr.replace(r'/','_')), 
                'Input/Output Bytes', 
                in_list, 'Input Bytes', 
                out_list, 'Output Butes', 
                times)

    print


if __name__ == '__main__':
    main()
