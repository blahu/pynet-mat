#!/usr/bin/env python
# Class 7
# Exercise 1b
# Author Mat
"""

   a. Create a program that opens the 'r1_cdp.txt' file and using regular expressions extracts the remote hostname, remote IP address, model, vendor, and device_type.

"""

import re
from pprint import pformat

a_file = open("CDP_DATA/sw1_cdp.txt")
cdp_data = a_file.read()


m = re.findall(r"Device ID: (.*)", cdp_data)
if m:
    print ("%12s: %s" % ( "remote_hosts" , pformat ( m )  ))


m = re.findall(r"IP address: (.*)", cdp_data)
if m:
    print ("%12s: %s" % ( "IPs" , pformat ( m)  ))

m = re.findall(r"Platform: (.*?),", cdp_data)
if m:
    print ("%12s: %s" % ( "platform" , pformat ( m)  ))
