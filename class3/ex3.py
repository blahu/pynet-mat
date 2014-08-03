#!/usr/bin/env python
# Class 3
# Exercise 3
# Author Mateusz Blaszczyk

import pprint

show_ip_int_brief = '''
Interface            IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset          up          up
FastEthernet1   unassigned      YES     unset          up          up
FastEthernet2   unassigned      YES     unset          down      down
FastEthernet3   unassigned      YES     unset          up          up
FastEthernet4    6.9.4.10         YES     NVRAM       up          up
NVI0                  6.9.4.10        YES     unset           up          up
Tunnel1            16.25.253.2     YES     NVRAM       up          down
Tunnel2            16.25.253.6     YES     NVRAM       up          down
Vlan1                unassigned      YES    NVRAM       down      down
Vlan10              10.220.88.1     YES     NVRAM       up          up
Vlan20              192.168.0.1     YES     NVRAM       down      down
Vlan100            10.220.84.1     YES     NVRAM       up          up
'''

# initialize array with all tuples
show_ip_list = []

for line in show_ip_int_brief.splitlines() :

    # skip header
    if "Interface" in line:
        continue

    # split line into chunks
    line_split = line.split()

    # skip lines not matching the pattern
    if len(line_split) != 6:
        continue

    # initialize variables
    interface, ip_addr, d1, d2, status, protocol = line_split

    # we are interested only in "up/up" state
    if status == "up" and protocol == "up":
        show_ip_list.append( (interface, ip_addr, status, protocol) )

pprint.pprint(show_ip_list)

    