#!/usr/bin/env python
# Class 7
# Exercise 1a
# Author Mat
"""

   a. Create a program that opens the 'r1_cdp.txt' file and using regular expressions extracts the remote hostname, remote IP address, model, vendor, and device_type.

"""

a_file = open("CDP_DATA/r1_cdp.txt")
cdp_data = a_file.read()
a_file.close()

import re
m = re.search(r"Device ID: (.*)", cdp_data)
if m:
    print m.group(1)
m = re.search(r"IP address: (.*)", cdp_data)
if m:
    print m.group(1)
m = re.search(r"Platform: (.*?) (.*?), +Capabilities: (.*)", cdp_data)
if m:
    print m.group(1)
    print m.group(2)
    print m.group(3)
