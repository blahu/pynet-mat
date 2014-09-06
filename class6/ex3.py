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

    if int(a) < 1 or int(a) > 223 or int(a) == 127:
        return False

    elif (  (int(b) not in range (0, 256)) or
            (int(c) not in range (0, 256)) or
            (int(d) not in range (0, 256))) :
        return False

    elif int(a) == 169 and int(b) == 254:
        return False

    return True


