#!/usr/bin/env python
# Class 3
# Exercise 4
# Author Mateusz Blaszczyk


"""
IV. Create a script that checks the validity of an IP address.  The IP address should be supplied on the command line.

    A. Check that the IP address contains 4 octets.
    B. The first octet must be between 1 - 223.
    C. The first octet cannot be 127.
    D. The IP address cannot be in the 169.254.X.X address space.
    E. The last three octets must range between 0 - 255.
 For output, print the IP and whether it is valid or not.
"""

import sys

valid = True
ip_addr = ''

# make sure there is only 1 argument on command line
if len(sys.argv) != 2:
	valid = False

else:
	ip_addr = sys.argv[1]
	octets = ip_addr.split(".")

	if len(octets) != 4:
		valid = False
	else:
		a,b,c,d = octets

		if int(a) < 1 or int(a) > 223 or int(a) == 127:
			valid = False

		elif int(b) not in range (0, 256) or int(c) not in range (0, 256) or int(d) not in range (0, 256) :
			valid = False

		elif int(a) == 169 and int(b) == 254:
			valid = False

if valid:
	print "[%s] is valid!" % ip_addr
else:
	print "[%s] is not valid!" % ip_addr