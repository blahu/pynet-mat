#!/usr/bin/env python
"""
Class 9
Exercise 3
Author mateusz

III. Write a new class, IPAddressWithNetmask, that is based upon the IPAddress
class created in exercise1 (i.e. use inheritance).  The netmask should be
stored in slash notation (i.e. /24). 
"""
__author__ = 'mateusz'

from cl6ex4 import padding
from cl8ex1 import validate_ip_address
from ex1 import IPAddress

class IPAddressWithNetmask(IPAddress):
    """
    Python class representing an IPAddressWithNetmask, inherited from IPAddress
    """
    def __init__(self, ip_addr_with_netmask):
        """
        Init method
        """
        try:
            ip_addr,netmask = ip_addr_with_netmask.split(r'/')
        except ValueError as e:
            raise ValueError

        # call the parent's __init__ method
        IPAddress.__init__(self, ip_addr)

        try:
            numeric_mask = int(netmask)
        except ValueError as e:
            raise ValueError

        if numeric_mask in range (1,33):
            # assign our new attribute
            self.netmask = r'/' + netmask
        else:
            raise ValueError


        if (not self.is_valid()):
            raise ValueError
            
        # split ip address into bytes
        self.ip_addr_list = self.ip_addr.split(".")

    def netmask_in_dotdecimal(self):
        """
        A. Create a new method in the IPAddressWithNetmask class that
        converts the slash notation netmask to dotted decimal.
        """

        netmask = int(self.netmask.split(r'/')[1])

        a_list = [ 2**7, 2**6, 2**5, 2**4, 2**3, 2**2, 2**1, 2**0]

        t1 = netmask / 8
        t2 = netmask % 8
        byte1 = 0
        byte2 = 0
        byte3 = 0
        byte4 = 0

        if t1 == 4:
            for i in range (8):
                byte1 += a_list[i]
                byte2 += a_list[i]
                byte3 += a_list[i]
                byte4 += a_list[i]

        if t1 == 3:
            for i in range (8):
                byte1 += a_list[i]
                byte2 += a_list[i]
                byte3 += a_list[i]
            if t2 > 0:
                for i in range (t2):
                    byte4 += a_list[i]

        if t1 == 2:
            for i in range (8):
                byte1 += a_list[i]
                byte2 += a_list[i]
            if t2 > 0:
                for i in range (t2):
                    byte3 += a_list[i]

        if t1 == 1:
            for i in range (8):
                byte1 += i * a_list[i]
            if t2 > 0:
                for i in range (t2):
                    byte2 += a_list[i]

        if t1 == 0:
            if t2 > 0:
                for i in range (t2):
                    byte1 += a_list[i]

        netmask = '{}.{}.{}.{}'.format(byte1,byte2,byte3,byte4)
        return netmask



if __name__ == '__main__':
    # tests
    ip_addr = '172.17.255.1/27'
    print ("Testing IPAddress= {}".format(ip_addr))

    test_ip = IPAddressWithNetmask (ip_addr)

    print ("Test1: ip_addr= {}". format(test_ip.ip_addr))
    print ("Test2: binary=  {}". format(test_ip.display_in_binary()))
    print ("Test3: hex=     {}". format(test_ip.display_in_hex()))
    print ("Test4: valid=   {}". format(test_ip.is_valid()))
    print ("Test5: masksize={}". format(test_ip.netmask))
    print ("Test5: netmask= {}". format(test_ip.netmask_in_dotdecimal()))

