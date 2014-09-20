#!/usr/bin/env python
# Class 8
# Exercise 2
# Author mat
__author__ = 'mateusz'

'''
    C. Write a script that processes the show_version output using this
    package.  It should return something similar to the following:

model:             881
os_version:    Version 15.0(1)M4
uptime:            uptime is 12 weeks, 5 days, 1 hour, 4 minutes
'''

import ex2.model
import ex2.os_version
import ex2.uptime

from sys import argv,exit

if __name__ == '__main__':

    try:
        fn = argv[1]
    except IndexError as e:
        exit("ERROR={}: Missing required argument".format(e))

    try:
        f = open( fn, "r")
    except IOError as e:
        exit("ERROR={}".format(e))

    show_version_data = f.read()
    f.close()

    test = [ 
        ex2.model.obtain_model,
        ex2.os_version.obtain_os_version,
        ex2.uptime.obtain_uptime,
    ]
    
    for t in test:

        print "{:<30} {}". format ( t.__name__.split('obtain_')[1] + '():', t(show_version_data))


