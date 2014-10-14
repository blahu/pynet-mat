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
import socket
import xmlrpclib
import sys
from pprint import pprint

def eapi_helper ( **eapi_params ):
    """ runs all commands via json rpc
    """
    eapi_user = eapi_params ['eapi_username']
    eapi_pass = eapi_params ['eapi_password']
    eapi_serv = eapi_params ['eapi_server']
    eapi_port = eapi_params ['eapi_port']
    eapi_comm = eapi_params ['eapi_commands']

    # build the url
    eapi_url = 'https://{}:{}@{}:{}/command-api'.format(eapi_user,
            eapi_pass,
            eapi_serv,
            eapi_port)

    # connect to the switch
    sw = jsonrpclib.Server (eapi_url)

    # run the cmds and return the dict
    try:
        resp = sw.runCmds(1, eapi_comm )[0]
    except socket.error as e:
        sys.exit("{}: {}". format(eapi_url, e))
    except xmlrpclib.ProtocolError as e:
        sys.exit (e)
    except jsonrpclib.jsonrpc.ProtocolError as e:
        sys.exit (e)

    return resp


if __name__ == '__main__':
    params =  { 'eapi_username': 'eapi',
                'eapi_password': 'eapu',
                'eapi_server'  : '1.1.1.3',
                'eapi_port'    : '443'
    }
    commands = ['show interfaces']
    params ['eapi_commands'] = commands

    resp = eapi_helper ( **params )

    for k in resp['interfaces'].keys():
        print "Interface={} inOctets={} outOctets={}".format( k, 
                resp[k]['interfaceCounters']['inOctets'], 
                resp[k]['interfaceCounters']['outOctets'] 
        )

