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

def get_counter_graph ( fn, title, in_list, in_title, out_list, out_title, times):
    '''
    Creates a graph using pygal in svg format
    Input/Output line graph in time.
    First it makes sure that if the data is of type counter, it recalculates the lists
    so that it prints the speed of change of the counter
    '''

    new_in_list = []
    new_out_list = []
    new_times = []

    for i in range(len(times)):
        # assume each list is the same, if IndexError than dont print anything

        if i > 0:
            new_times.append    (    times [i] )
            new_in_list.append  (  in_list [i] - prev_in )
            new_out_list.append ( out_list [i] - prev_out )
        
            prev_in = in_list[i]
            prev_out = out_list[i]
        else:
            # first time over , just initiate the variables
            prev_in  = in_list [0]
            prev_out = out_list [0]
        #ENDOF if i > 0:

    #ENDOF for i in range(len(times)):

    return get_iface_graph ( fn, title, new_in_list, in_title, 
                                        new_out_list, out_title, new_times)

#ENDOF def get_counter_graph

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

            counter = {
                    'ifInOctets': [],
                    'ifOutOctets' : [],
                    'ifInUcastPkts': [],
                    'ifOutUcastPkts' : [],
            }
            times = []

            max_size = 12
            seconds = 5*60

            for j in range(max_size):
                # Loop for $seconds

                print 'j={}'.format(j)
                
                # for x-labels
                times.append('{}s'.format(j*seconds))

                for oid in counter.keys():

                    # get snmp ifInOctets.IfIndex==1
                    c = get_snmp_data ( router_data, OIDS[oid] + idx)
                    if c:
                        print '{}={}'.format(oid,c)

                    counter[oid] = rrd_add (counter[oid], int(c), max_size)

                # sleep seconds
                sleep(seconds)
            #EMDOF:for i in (range(10):
 
            get_counter_graph ( '{}_{}_Octets.svg'.format(router,if_descr.replace(r'/','_')), 
                'Input/Output Bytes', 
                counter['ifInOctets'], 'Input Bytes', 
                counter['ifOutOctets'], 'Output Bytes', 
                times)
            get_counter_graph ( '{}_{}_Packets.svg'.format(router,if_descr.replace(r'/','_')), 
                'Input/Output Unicast Packets', 
                counter['ifInUcastPkts'], 'Input Packets', 
                counter['ifOutUcastPkts'], 'Output Packets', 
                times)

    print


if __name__ == '__main__':
    main()
