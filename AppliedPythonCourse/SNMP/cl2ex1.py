#!/usr/bin/env python
# Class 2
# Exercise 1
# Author mblaszczyk
'''
1. Using SNMPv3 create a script that detects changes to the running
configuration.  If the running configuration is changed, then send an email
notification to yourself identifying the router that changed and the time that
it changed.
'''

import sys

from snmp_helper import snmp_get_oid,snmp_get_oid_v3,snmp_extract

from ROUTERS import ROUTERS
from OIDS import OIDS


if __name__ == '__main__':

    for router, router_data in ROUTERS.items():
        if sys.argv[1] in router:

            #skip non v3 routers
            if router_data['snmp_v'] <3:
                continue

            print
            print router

            # create SNMPv3 vars
            snmp_user = ('pysnmp', 'galileo1', 'galileo1')

            # create snmp_device tuple
            snmp_device = ( router_data['IP'], router_data['SNMP Port'])
            
            # change 100th of a sec into sec
            div = 100

            # get snmp ccmHistoryRunningLastChanged
            snmp_data = snmp_get_oid_v3 (
                    snmp_device, snmp_user, OIDS['ccmHistoryRunningLastChanged'])
            if snmp_data:
                running_last_changed_ticks = int (snmp_extract (snmp_data)) / div
            else:
                exit(1)

            snmp_data = snmp_get_oid_v3 (
                    snmp_device, snmp_user, OIDS['ccmHistoryRunningLastSaved']) 
            if snmp_data:
                running_last_saved_ticks = int (snmp_extract (snmp_data)) / div
            else:
                exit(1)

            snmp_data = snmp_get_oid_v3 (
                    snmp_device, snmp_user, OIDS['ccmHistoryStartupLastChanged']) 
            if snmp_data:
                startup_last_changed_ticks = int (snmp_extract (snmp_data)) / div
            else:
                exit(1)

            # get snmp uptime
            snmp_data = snmp_get_oid_v3 (
                    snmp_device, snmp_user, OIDS['sysUpTime']) 
            if snmp_data:
                uptime_ticks = int (snmp_extract (snmp_data)) / div
            else:
                exit(1)


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
            
            recipient = 'blahu77@gmail.com'
            sender    = 'blahu77@gmail.com'
            subject = '[' + router + ']: Config Alert'
            smtp_server = 'mail1.eircom.net'
            message = '''
            It looks like the Running Config on {} has been changed.
            You should look into that.
            It happened more less {} second(s) ago.
            '''.format ( router, time_since_running_changed )

            if running_last_changed_ticks > running_last_saved_ticks:
                print "Running Config has been changed"

                # this test is very arbitrary:
                if running_last_changed_ticks < 10:
                    # maybe just booted?
                    message += '''
                    There is a slight chance that the router was just rebooted.
                    '''
                
                from email_helper import send_mail
                send_mail ( recipient, subject, message, sender, smtp_server)

            else:
                print "Running Config has not been changed since last Running Config save"
                if startup_last_changed_ticks > running_last_changed_ticks:
                    print "Startup Config has been saved since last Running Config change"
                else:
                    print "Startup Config has not been saved since last Running Config change"


    print

