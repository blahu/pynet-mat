#!/usr/bin/env python
# 
# Class     4
# Exercise  1
# Author    Mateusz Blaszczyk

""" I. Prompt a user to input an IP address.  Re-using some of the
code from class3, exercise4--determine if the IP address is valid.
Continue prompting the user to re-input an IP address until a valid IP
address is input. """

import sys

print sys.argv[0]
print "...begin...\n"

ip_addr = ''


while True:
    # initialize the valid flag
    valid = True

    # prompt user for IP addres
    ip_addr = raw_input ("Please enter a valid IP address: ")

    octets = ip_addr.split(".")

    if len(octets) != 4:
        valid = False
    else:
        a,b,c,d = octets

        if int(a) < 1 or int(a) > 223 or int(a) == 127:
            valid = False

        elif int(b) not in range (0, 256) or \
            int(c) not in range (0, 256) or \
            int(d) not in range (0, 256) :
                valid = False

        elif int(a) == 169 and int(b) == 254:
            valid = False

    if valid:
        # break if valid, otherwise rinse and repeat
        print "[%s] is valid!" % ip_addr
        break
    else:
        print "[%s] is not valid!" % ip_addr



print "...end...\n"