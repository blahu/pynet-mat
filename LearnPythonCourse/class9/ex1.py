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

class IPAddress(object):
    """
    Python class representing an IPAddress
    """
    def __init__(self, ip_address):
        """
        Init method
        """
        self.ip_addr = ip_address


if __name__ == '__main__':

    # tests

    test_ip = IPAddress ('192.168.1.1')

    print test_ip.ip_addr 
