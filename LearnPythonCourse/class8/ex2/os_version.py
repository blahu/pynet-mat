#!/usr/bin/env python
# Class 8
# Exercise 2
# Author mat
__author__ = 'mateusz'

import re

'''
1. Function1 = obtain_os_version -- process the show version output and return
the OS version (Version 15.0(1)M4) else return None.
'''

def obtain_os_version( show_ver_data ):
    '''
    Processes show version data from cisco router and obtains IOS version
    '''
    for line in show_ver_data.splitlines():
        m = re.search(r'^Cisco.*?Version (.*?),', line)
        if m:
            return m.group(1)
    return None

if __name__ == '__main__':
    test = obtain_os_version

    ''' test if that works '''

    from sys import argv
    fn = argv[1]

    f = open( fn, "r")


    print test(f.read())
    f.close()
