#!/usr/bin/env python
# Class 1
# Exercise 3b
# Author mblaszczyk


from snmp_helper import snmp_get_oid,snmp_extract

from ROUTERS import ROUTERS
from OIDS import OIDS

for router, router_data in ROUTERS.items():
    print
    print router
    
    # create snmp_device tuple
    snmp_device = ( router_data['IP'], router_data['SNMP Community'], router_data['SNMP Port'])
    
    # get snmp ccmHistoryRunningLastChanged
    snmp_data_RunningLastChanged = snmp_get_oid (snmp_device,OIDS['ccmHistoryRunningLastChanged']) 
    snmp_data_RunningLastSaved = snmp_get_oid (snmp_device,OIDS['ccmHistoryRunningLastSaved']) 
    snmp_data_StartupLastChanged = snmp_get_oid (snmp_device,OIDS['ccmHistoryStartupLastChanged']) 

    # get snmp uptime
    snmp_data_uptime = snmp_get_oid (snmp_device,OIDS['sysUpTime']) 

    running_last_changed_ticks = snmp_extract (snmp_data_RunningLastChanged)
    running_last_saved_ticks = snmp_extract (snmp_data_RunningLastSaved)
    startup_last_changed_ticks = snmp_extract (snmp_data_StartupLastChanged)
    uptime_ticks = snmp_extract (snmp_data_uptime)

    print "%10s uptime               " % (uptime_ticks)
    print "%10s running last_changed " % (running_last_changed_ticks)
    print "%10s running last_saved   " % (running_last_saved_ticks)
    print "%10s startup last_changed " % (startup_last_changed_ticks)


    if startup_last_changed_ticks == running_last_saved_ticks and running_last_saved_ticks > running_last_changed_ticks:
        print "Startup Config has been saved since last Running Config change"
    else:
        print "Running Config has been changed and not saved"
