#!/usr/bin/env python
# Class 8
# Exercise 2
# Author mat
__author__ = 'mateusz'

import re

'''
3. Function3 = obtain_model -- process the show version output and return the
model (881) else return None
'''

def obtain_model( show_ver_data ):
    '''
    Processes show version data from cisco router and obtains model
    '''
    for line in show_ver_data.splitlines():
        m = re.search(r'^Cisco ([a-zA-Z0-9-_]+) (.*?) memory.$', line)
        if m:
            return m.group(1)
    return None

if __name__ == '__main__':
    test = obtain_model

    ''' test if that works '''

    from sys import argv
    fn = argv[1]

    f = open( fn, "r")
    print test(f.read())
    f.close()
