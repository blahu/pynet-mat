#!/usr/bin/env python
"""
Class 6
Exercise 3
Author Mat
"""

"""
3a.Convert the IP address validation code (Class4, exercise1) into a function,
take one variable 'ip_address' and return either True or False (depending on
whether 'ip_address' is a valid IP).  Only include IP address checking in the
function--no prompting for input, no printing to standard output.
"""


def validate_ip_address (ip_address) :

    octets = ip_address.split(".")

    if len(octets) != 4:
        return False
    else:
        a,b,c,d = octets

    try:
        int_a = int(a)
        int_b = int(b)
        int_c = int(c)
        int_d = int(d)

    except ValueError as e:
        # int() conversion failed:
        return False

    # check 1st octet
    if int_a < 1 or int_a > 223 or int_a == 127:
        return False

    # check 2nd 3rd and 4th octet
    elif (  (int_b not in range (0, 256)) or
            (int_c not in range (0, 256)) or
            (int_d not in range (0, 256))) :
        return False

    # check 169.254.x.x 
    elif int_a == 169 and int_b == 254:
        return False

    # validated as an IP address!
    return True


