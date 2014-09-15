#!/usr/bin/env python
# Class 1
# Exercise 3b
# Author mblaszczyk

import sys

from snmp_helper import snmp_get_oid,snmp_extract

from ROUTERS import ROUTERS
from OIDS import OIDS

for router, router_data in ROUTERS.items():
    if router not in sys.argv[1]:
        continue
    print
    print router
    
    # create snmp_device tuple
    snmp_device = ( router_data['IP'], router_data['SNMP Community'], router_data['SNMP Port'])
    
    # get snmp ccmHistoryRunningLastChanged
    snmp_data_RunningLastChanged = snmp_get_oid (snmp_device,OIDS['ccmHistoryRunningLastChanged']) 
    snmp_data_RunningLastSaved   = snmp_get_oid (snmp_device,OIDS['ccmHistoryRunningLastSaved']) 
    snmp_data_StartupLastChanged = snmp_get_oid (snmp_device,OIDS['ccmHistoryStartupLastChanged']) 

    # get snmp uptime
    snmp_data_uptime = snmp_get_oid (snmp_device,OIDS['sysUpTime']) 

    div = 100
    running_last_changed_ticks = int (snmp_extract (snmp_data_RunningLastChanged)) / div
    running_last_saved_ticks   = int (snmp_extract (snmp_data_RunningLastSaved))   / div
    startup_last_changed_ticks = int (snmp_extract (snmp_data_StartupLastChanged)) / div
    uptime_ticks               = int (snmp_extract (snmp_data_uptime))             / div

    print "{:10} uptime               ".format (uptime_ticks               )
    print "{:10} running last_changed ".format (running_last_changed_ticks )
    print "{:10} running last_saved   ".format (running_last_saved_ticks   )
    print "{:10} startup last_changed ".format (startup_last_changed_ticks )


    time_since_startup_saved = (uptime_ticks - startup_last_changed_ticks ) 
    print "Time since startup saved {}".format(time_since_startup_saved)

    time_since_running_changed = (uptime_ticks - running_last_changed_ticks) 
    print "Time since running changed {}".format(time_since_running_changed)

    time_since_running_saved = (uptime_ticks - running_last_saved_ticks ) 
    print "Time since running saved {}".format(time_since_running_saved)
    
    if running_last_changed_ticks > running_last_saved_ticks:
        print "Running Config has been changed"
    else:
        print "Running Config has not been changed since last Running Config save"
        if startup_last_changed_ticks > running_last_changed_ticks:
            print "Startup Config has been saved since last Running Config change"
        else:
            print "Startup Config has not been saved since last Running Config change"


print
