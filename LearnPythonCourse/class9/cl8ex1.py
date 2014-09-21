#!/usr/bin/env python
"""
Class 8, was 6
Exercise 1, was 3
Author Mat
"""
__author__ = 'mateusz'

"""
Class6
"""
"""
Class8
I. Re-using the IP address validation function created in Class #6, exercise3;
create a Python module that contains only this one ip validation function.

     A. Modify this Python module such that you add a set of tests into the
module.  Use the __name__ == '__main__' technique to separate the test code
from the function definition.  In your test code, check the validity of each of
the following IP addresses (False means it should fail; True means it should
pass the IP address validation).

    test_ip_addresses = {
        '192.168.1' : False,
        '10.1.1.' : False,
        '10.1.1.x' : False,
        '0.77.22.19' : False,
        '-1.88.99.17' : False,
        '241.17.17.9' : False,
        '127.0.0.1' : False,
        '169.254.1.9' : False,
        '192.256.7.7' : False,
        '192.168.-1.7' : False,
        '10.1.1.256' : False,
        '1.1.1.1' : True,
        '223.255.255.255': True,
        '223.0.0.0' : True,
        '10.200.255.1' : True,
        '192.168.17.1' : True,
    }

    B. Execute this module--make sure all of the tests pass.

    C. Import this module into the Python interpreter shell.  Make sure the
test code does not execute.  Also test that you can still correctly call the ip
validation function.
"""


def validate_ip_address (ip_address) :
    """
    3a.Convert the IP address validation code (Class4, exercise1) into a function,
    take one variable 'ip_address' and return either True or False (depending on
    whether 'ip_address' is a valid IP).  Only include IP address checking in the
    function--no prompting for input, no printing to standard output.
    """

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

#ENDOF def validate_ip_address

if __name__ == '__main__':

    test_ip_addresses = {
        '192.168.1' : False,
        '10.1.1.' : False,
        '10.1.1.x' : False,
        '0.77.22.19' : False,
        '-1.88.99.17' : False,
        '241.17.17.9' : False,
        '127.0.0.1' : False,
        '169.254.1.9' : False,
        '192.256.7.7' : False,
        '192.168.-1.7' : False,
        '10.1.1.256' : False,
        '1.1.1.1' : True,
        '223.255.255.255': True,
        '223.0.0.0' : True,
        '10.200.255.1' : True,
        '192.168.17.1' : True,
    }

    for test_ip, test_result  in test_ip_addresses.items():
        
        result = validate_ip_address ( test_ip )

        if result == test_result:
            result_text = 'ok'
        else:
            result_text = 'failed, was {} should be {}'.format (result, test_result)

        print "{:.<30}{}".format (test_ip + ' ', result_text)
