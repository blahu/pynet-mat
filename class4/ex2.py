#!/usr/bin/env python
# Class 4
# Exercise 2
# Author Mateusz Blaszczyk

""" II. Parse the below 'show version' data and obtain the following items
(vendor, model, os_version, uptime, and serial_number).  Try to make your
string parsing generic i.e. it would work for other Cisco IOS devices.  
The following are reasonable strings to look for: 
'Cisco IOS Software' for vendor and os_version 
'bytes of memory' for model 
'Processor board ID' for serial_number 
'uptime is ' for uptime 

Store these variables (vendor, model, os_version, uptime, and serial_number) 
in a dictionary.  
Print the dictionary to standard output when done. 
Note, "Cisco IOS Software...Version 15.0(1)M4...(fc1)" is one line. """

from pprint import pprint

show_version_data = """Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc
Compiled Fri 29-Oct-10 00:02 by prod_rel_team
ROM: System Bootstrap, Version 12.4(22r)YB5, RELEASE SOFTWARE (fc1)

twb-sf-881 uptime is 7 weeks, 5 days, 19 hours, 23 minutes

System returned to ROM by reload at 15:33:36 PST Fri Feb 28 2014
System restarted at 15:34:09 PST Fri Feb 28 2014
System image file is "flash:c880data-universalk9-mz.150-1.M4.bin"
Last reload type: Normal Reload
Last reload reason: Reload Command

Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX1000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)

License Info:
License UDI:
-------------------------------------------------
Device#   PID                   SN
-------------------------------------------------
*0        CISCO881-SEC-K9       FTX1000038X

License Information for 'c880-data'
    License Level: advipservices   Type: Permanent
    Next reboot license Level: advipservices

Configuration register is 0x2102"""

dictionary = {}

for line in show_version_data.splitlines():

    # First look for version - collect vendor and version 
    if 'Cisco IOS Software' in line:

        # split line with comma
        line_split = line.split(',')

        # first element is 'Cisco IOS Software'
        # and first element of that is Cisco - vendor
        dictionary ['vendor'] = line_split[0].split()[0]

        # os_version is 3rd element 'Version 15.0(1)M4'
        # end 2nd element of that is 15... - os_version
        dictionary ['os_version'] = line_split[2].split()[1]

    elif 'bytes of memory' in line:
        # split line with space
        line_split = line.split()

        # 2nd element is model
        dictionary ['model'] = line_split[1]

    elif 'Processor board ID' in line:
        # split line with space
        line_split = line.split()

        # last element is the Serial No
        dictionary ['serial_number'] = line_split[-1]

    elif 'uptime is' in line:
        # split line with space but only the first 3
        line_split = line.split (' ', 3)

        # last (3rd) element is the uptime
        dictionary ['uptime'] = line_split[3]

pprint (dictionary)
