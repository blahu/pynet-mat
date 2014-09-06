#!/usr/bin/env python
"""
Class 6
Exercise 5
Author Mat
"""

"""
5. Write a program that prompts a user for an IP address, then checks if the IP
address is valid, and then converts the IP address to binary (dotted decimal
format).  Re-use the functions created in exercises 3 and 4 ('import' the
functions into your new program).
"""

import sys
from ex3 import validate_ip_address
from ex4 import dotted_dec_to_bin


# initialize ip_addr
ip_addr = ''

# initialize the valid flag
valid = False

while not valid:
    # prompt user for IP addres
    ip_addr = raw_input ("Please enter a valid IP address: ")

    if validate_ip_address(ip_addr):
        valid = True
        print "%s in binary is %s" % (ip_addr, dotted_dec_to_bin(ip_addr))
    else:
        print "%s is not valid!" % ip_addr
