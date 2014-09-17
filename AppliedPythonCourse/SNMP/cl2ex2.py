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

iface_stats = {}

def main():

    for router, router_data in ROUTERS.items():
        if sys.argv[1] in router:

            print
            print router
            i = '.1'

            # get current time
            from time import strftime
            curr_time = strftime('%Y-%m-%d %H:%M:%S')
            print 'Current Time={}'.format(curr_time)

            # get snmp ifDescr.IfIndex==1
            if_descr = get_snmp_data ( router_data, OIDS['ifDescr'] + i)
            if if_descr:
                print 'ifDescr={}'.format(if_descr)

            # get snmp ifInOctets.IfIndex==1
            if_oct_in = get_snmp_data ( router_data, OIDS['ifInOctets'] + i)
            if if_oct_in:
                print 'ifInOctets={}'.format(if_oct_in)

            # get snmp ifOutOctets.IfIndex==1
            if_oct_out = get_snmp_data ( router_data, OIDS['ifOutOctets'] + i)
            if if_oct_out:
                print 'ifInOctets={}'.format(if_oct_out)
    print


if __name__ == '__main__':
    main()
