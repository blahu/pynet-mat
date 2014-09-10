#!/usr/bin/env python
# Class 7
# Exercise 2
# Author Mat
"""


2. In the following directory there is a file 'ospf_single_interface.txt':

    https://github.com/ktbyers/pynet/tree/master/learnpy_ecourse/class7/OSPF_DATA

    Open this file and extract the interface, IP address, area, type, cost,
    hello timer, and dead timer.  Use regular expressions to accomplish your
    extraction.

    Your output should look similar to the following:

    Int:       GigabitEthernet0/1
    IP:        172.16.13.150/29
    Area:    30395
    Type:    BROADCAST
    Cost:    1
    Hello:   10
    Dead:   40
"""
import re

a_file = open("OSPF_DATA/ospf_single_interface.txt")
cdp_data = a_file.read()
a_file.close()

m = re.search(r"^([^ ]+?) is ", cdp_data)
if m:
    print m.group(1)

m = re.search(r"Internet Address ([0-9\.\/]+), Area ([0-9]+),", cdp_data)
if m:
    print m.group(1)
    print m.group(2)

m = re.search(r"Network Type (.+?), Cost: ([0-9]+)" , cdp_data)
if m:
    print m.group(1)
    print m.group(2)

m = re.search(r"Hello ([0-9]+), Dead ([0-9]+), Wait" , cdp_data)
if m:
    print m.group(1)
    print m.group(2)
