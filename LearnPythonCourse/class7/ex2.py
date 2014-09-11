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


def re_search( regexp, string):
    """ 
    Searches string for regexp
    Returns tuple or False
    """
    try:
        m = re.search(regexp, string)
    except TypeError as e:
        return False
    if m:
        return m.groups()
    return False

OSPF_REGEXP = {
        'Int'  : r"^([^ ]+?) is ",
        'IP'   : r"Internet Address ([0-9\.\/]+), ",
        'Area' : r", Area ([0-9]+),",
        'Type' : r"Network Type (.+?),",
        'Cost' : r", Cost: ([0-9]+)",
        'Hello': r"Hello ([0-9]+),",
        'Dead' : r"Dead ([0-9]+), Wait",
}


def print_ospf_interface (ospf_interface):
    """
    Expects string matching something like this:

    GigabitEthernet0/0.2561 is up, line protocol is up
    Internet Address 10.22.0.117/30, Area 303953, Attached via Network Statement
    [...]
    Process ID 1, Router ID 10.90.3.38, Network Type POINT_TO_POINT, Cost: 1
    Youngest key id is 1

    prints 
    
    Int:       GigabitEthernet0/1
    IP:        172.16.13.150/29
    Area:    30395
    Type:    BROADCAST
    Cost:    1
    Hello:   10
    Dead:   40
    """


    OSPF_HEADERS = ['Int', 'IP', 'Area', 'Type', 'Cost', 'Hello', 'Dead' ]
    
    for key in OSPF_HEADERS:
        m = re_search(OSPF_REGEXP[ key ] , ospf_interface)
        if m:
            print "%-5s: %s" % ( key,  m[0]) 
    print


if __name__ == "__main__":
    f = open("OSPF_DATA/ospf_single_interface.txt") 
    ospf_interface = f.read()
    f.close()

    print_ospf_interface (ospf_interface)
