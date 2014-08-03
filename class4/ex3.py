#!/usr/bin/env python
# Class 4
# Exercise 3
# Author Mateusz Blaszczyk

""" III. Create a program that converts the following uptime strings to a time
in seconds.

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes' 
uptime2 = '3750RJ uptime is 1 hour, 29 minutes' 
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes' 
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8hours, 23 minutes'

For each of these strings store the uptime in a dictionary using the device
name as the key.

During this conversion process, you will have to convert strings to integers.
For these string to integer conversions use try/except to catch any string to
integer conversion exceptions.

For example: 
int('5') works fine 
int('5 years') generates a ValueError exception.

Print the dictionary to standard output. """

uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes' 
uptime2 = '3750RJ uptime is 1 hour, 29 minutes' 
uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes' 
uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8hours, 23 minutes'

d = {}
for line in (uptime1, uptime2,uptime3,uptime4):

    # split each line and assign router name and uptime variables
    line_split = line.split(' ', 3)
    router = line_split[0]
    uptime = line_split[3]

    # split uptime with comma
    uptime_split = uptime.split(',')

    # we will store no of sec in this variable:
    uptime_in_sec = 0

    for t in uptime_split:

        # strip leading space
        t.strip()

        if 'minutes' in t:
            try:
                uptime_in_sec += 60 * int( t.split(' minutes')[0]  )
            except ValueError as e:
                print "Bad Translation - " + str(e)

        elif 'hours' in t:
            try:
                uptime_in_sec += 60 * 60 * int( t.split(' hours')[0]  )
            except ValueError as e:
                print "Bad Translation - " + str(e)

        elif 'days' in t:
            try:
                uptime_in_sec += 24 * 60 * 60 * int( t.split(' days')[0]  )
            except ValueError as e:
                print "Bad Translation - " + str(e)

        elif 'weeks' in t:
            try:
                uptime_in_sec += 7 * 24 * 60 * 60 * int( t.split(' weeks')[0]  )
            except ValueError as e:
                print "Bad Translation - " + str(e)

        elif 'years' in t:
            try:
                uptime_in_sec += 52 * 7 * 24 * 60 * 60 * int( t.split(' years')[0]  )
            except ValueError as e:
                print "Bad Translation - " + str(e)




    d [router] = uptime_in_sec

print
import pprint
pprint.pprint(d)
print
