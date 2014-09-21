#!/usr/bin/env python
"""
Class 9
Exercise 1
Author mateusz

I. Create a Python class representing an IPAddress.  The class should have only
one initialization variable--an IP address in dotted decimal formation.  You
should be able to do the following with your class:
"""
__author__ = 'mateusz'

from cl6ex4 import padding
from cl8ex1 import validate_ip_address

class IPAddress(object):
    """
    Python class representing an IPAddress
    """
    def __init__(self, ip_address):
        """
        Init method
        """
        self.ip_addr = ip_address

        if (not self.is_valid()):
            raise ValueError
            
        # split ip address into bytes
        self.ip_addr_list = self.ip_addr.split(".")

    def display_in_binary(self):
        """
        returns the IP address in dotted binary format (each octet should be
        eight binary digits in length).
        """
        return self.display_in( bin, 8)
    
    def display_in_hex(self):
        """
        returns the IP address in dotted hex format (each octet should be
        two hex digits in length).
        """
        return self.display_in( hex, 2, ":")
    
    def display_in(self, func=bin, upto=8, sep="."):
        # blank list to store bytes of ip
        bytes_list = []

        for byte in self.ip_addr_list:   
            # convert to "func" and strip off first "0b" for binary 0x for hex etc
            just_byte = func(int(byte))[2:]

            # add to list
            bytes_list.append( padding (just_byte, pad_upto=upto) )

        # join the list making it dotted format
        return sep.join(bytes_list)

    def is_valid(self):
        """
        C. Re-using the IP address validation code from class8,
        exercise1--create an is_valid() method that returns either True or
        False depending on whether the IP address is valid.
        """
        return validate_ip_address (self.ip_addr)


if __name__ == '__main__':
    # tests
    test_ip = IPAddress ('192.168.1.1')

    print ("Test1: ip_addr= {}". format(test_ip.ip_addr))
    print ("Test2: binary=  {}". format(test_ip.display_in_binary()))
    print ("Test3: hex=     {}". format(test_ip.display_in_hex()))
    print ("Test4: valid=   {}". format(test_ip.is_valid()))

