#!/usr/bin/env python
# Class 8
# Exercise 2
# Author mat
__author__ = 'mateusz'

import re

'''
2. Function2 = obtain_uptime -- process the show version output and return the
network device's uptime string (uptime is 12 weeks, 5 days, 1 hour, 4 minutes)
else return None.
'''

def obtain_uptime( show_ver_data ):
    '''
    Processes show version data from cisco router and obtains uptime
    '''
    for line in show_ver_data.splitlines():
        m = re.search(r'^[a-zA-Z0-9-_]+ uptime is (.*)', line)
        if m:
            return m.group(1)
    return None

if __name__ == '__main__':
    test = obtain_uptime

    ''' test if that works '''

    from sys import argv
    fn = argv[1]

    f = open( fn, "r")
    print test(f.read())
    f.close()
