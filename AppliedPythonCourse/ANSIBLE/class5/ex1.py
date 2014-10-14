#!/usr/bin/env python
# Class 5
# Exercise 1
# Author mat
"""
1. Use Arista's eAPI to obtain 'show interfaces' from the switch.  Parse the
'show interfaces' output to obtain the 'inOctets' and 'outOctets' fields for
each of the interfaces on the switch.  Accomplish this directly using
jsonrpclib.
"""

__author__ = 'mateusz'


import jsonrpclib



if __name__ = '__main__':

    eapi_username = 'eapi'
    eapi_password = 'eapu'
    eapi_server = '10.1.1.3'
    eapi_port = '80'



    eapi_url = 'http://{}:{}@{}:{}/command_api'.format(eapi_username,
            eapi_password,
            eapi_password,
            eapi_server,
            eapi_port)
    conn = jsonrpclib.Server (eapi_url)
