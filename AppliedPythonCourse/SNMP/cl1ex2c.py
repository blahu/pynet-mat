#!/usr/bin/env python
# Class 1
# Exercise 2c
# Author mblaszczyk


from snmp_helper import snmp_get_oid,snmp_extract

ROUTERS = {
    'pynet-rtr1' : {
        'IP' : '50.242.94.227',
        'SNMP Port' : 7961,
        'SNMP Community' : 'galileo',
    },
    'pynet-rtr2' : {
        'IP' : '50.242.94.227',
        'SNMP Port' : 8061,
        'SNMP Community' : 'galileo',
    },
}

OIDS={'sysDescr':'1.3.6.1.2.1.1.1.0','sysName':'1.3.6.1.2.1.1.5.0'}

for router, router_data in ROUTERS.items():
    print
    print router
    
    # create snmp_device tuple
    snmp_device = ( router_data['IP'], router_data['SNMP Community'], router_data['SNMP Port'])
    
    # list interesting oids:
    for oid_name,oid in OIDS.items():
        snmp_data = snmp_get_oid (snmp_device, oid)
        print
        print oid_name
        print snmp_extract (snmp_data)
