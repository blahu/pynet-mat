#!/usr/bin/env python
# Class 7
# Exercise 3
# Author Mat
"""


3.  In the following directory there is a file 'ospf_data.txt':

    https://github.com/ktbyers/pynet/tree/master/learnpy_ecourse/class7/OSPF_DATA

    This file contains the output from 'show ip ospf interface'.  Using
    functions and regular expressions parse this output to display the
    following (note, I ended up using re.split() as part of the solution to
    this problem):

        Int: Loopback0
        IP: 10.90.3.38/32
        Area: 30395
        Type: LOOPBACK
        Cost 1

        Int: GigabitEthernet0/1
        IP: 172.16.13.150/29
        Area: 30395
        Type: BROADCAST
        Cost 1
        Hello: 10
        Dead: 40

        Int: GigabitEthernet0/0.2561
        IP: 10.22.0.117/30
        Area: 30395
        Type: POINT_TO_POINT
        Cost 1
        Hello: 10
        Dead: 40

"""
import re
import pprint
from ex2 import print_ospf_interface

f = open("OSPF_DATA/ospf_data.txt")
ospf_data = f.read()
f.close()


# re.split the long output where the line starts with <CR>"nonspace" etc. <CR>Giga.. <CR>L 
# Make sure that the first character "non space" is taken into account (?=...)
# Lastly get rid of first empty line
m = re.split ( r"\n(?=[^ ])", ospf_data)[1:]
##pprint.pprint ( m )

for ospf_interface in m:
    print_ospf_interface (ospf_interface)
