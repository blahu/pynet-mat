#!/usr/bin/env python
# Class 5
# Exercise 2
# Author Mateusz Blaszczyk


print "Class 5, Exercise 2"

"""
Create a second program that expands upon the program from Exercise I.

This program will keep track of which network devices are physically adjacent to each other (physically connected to each other).  

You will accomplish this by adding a new field (adjacent_devices) to your network_devices inner dictionary.  adjacent_devices will be a list of hostnames that a given network device is physically connected to.  

For example, the dictionary entries for 'R1' and 'SW1' should look as follows:

    'R1': {'IP': '10.1.1.1',
                    'adjacent_devices': ['SW1'],
                    'device_type': 'Router',
                    'model': '881',
                    'vendor': 'Cisco'},

     'SW1': {'IP': '10.1.1.22',
                    'adjacent_devices': ['R1', 'R2', 'R3', 'R4', 'R5'],
                    'device_type': 'Switch',
                    'model': 'WS-C2950-24',
                    'vendor': 'cisco'},
"""

from pprint import pprint

# this will allow me to reference the variables *_show_cdp_* without prefix
# kirk.cdp_data
from kirk.cdp_data import *


all_cdp_data = { 
    'SW1':  sw1_show_cdp_neighbors_detail,
    'R1':   r1_show_cdp_neighbors_detail,
    'R2':   r2_show_cdp_neighbors_detail,
    'R3':   r3_show_cdp_neighbors_detail,
    'R4':   r4_show_cdp_neighbors_detail,
    'R5':   r5_show_cdp_neighbors_detail,
}


# initialize dict
network_devices = {}

count = 0
for host, cdp_detail in all_cdp_data.items():

    # initialiase device's dict if not yet exists
    # device can be initialised either via main loop (for host) or 
    # when a neighbour is found in CDP data
    if host not in network_devices:
        network_devices [ host ] = {}

    # initialize the list of neighbours
    network_devices [ host ]['adjacent_devices'] = []

    # each entry is separated by long ----....- 
    cdp_detail_split = cdp_detail.split('-------------------------')

    for d in cdp_detail_split:
        # make sure we process don't long lists of nothing
        d = d.strip()

        device = ''
        for line in d.splitlines():
            line = line.strip()

            if "Device ID:" in line:
                # split line against ":", device id is the last one
                device = line.split(":")[-1].strip()

                # initialiase device's dict if not yet exists
                if device not in network_devices:
                    network_devices [ device ] = {}

                # add to topology
                network_devices [ host ] [ 'adjacent_devices' ].append (device)

            elif "IP address:" in line:
                # split line against ":", ip is the last one
                ip = line.split(":")[-1].strip()
                network_devices [ device ]['ip'] = ip
            
            elif "Platform:" in line:
                # first split with "," 
                platform, capabilities = line.split(",")

                # split platform against ":", model is the last one
                model = platform.split(":")[-1].strip()
                vendor, model = model.split()
                network_devices [ device ]['model'] = model
                network_devices [ device ]['vendor'] = vendor.capitalize()

                # split line against ":", device_type is the last one
                device_types = capabilities.split(":")[-1].strip()
                # take only first of device_types
                network_devices [ device ]['device_type'] = device_types.split()[0]
            else:
                pass
                #print "WTF"

pprint ( network_devices )

