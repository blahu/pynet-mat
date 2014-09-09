#!/usr/bin/env python
"""
Class 6
Exercise 4
Author Mat
"""

"""
4. Create a function using your dotted decimal to binary conversion code from
Class3, exercise1.  In the function--do not prompt for input and do not print
to standard output.  The function should take one variable 'ip_address' and
should return the IP address in dotted binary format always padded to eight
binary digits (for example, 00001010.01011000.00010001.00010111).  You might
want to create other functions as well (for example, the zero-padding to eight
        binary digits).
"""

def padding ( string, pad_char='0', pad_upto=8, before=True, after=False):
    '''
    Padding will pad the 'string' with 'pad_char' before or after
    so that the total length of the string will be pad_upto
    after takes precedence, but before=True is default value
    '''

    # calculate padding of "0s"
    padding = pad_char * (pad_upto - len(string))

    # pad:
    if after:
        return string + padding
    if before:
        return padding + string

def dotted_dec_to_bin (ip_address):

    # split ip address into bytes
    l = ip_address.split(".")

    # blank list to store binary ip
    bin_ip = []

    for byte in l:   

        # convert to binary and strip off first "0b"
        just_byte = bin(int(byte))[2:]

        # add to list
        bin_ip.append( padding (just_byte) )

    # join the list making it dotted format
    return ".".join(bin_ip)

