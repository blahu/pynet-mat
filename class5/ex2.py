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

# code-reuse, get_show_version from class4/ex2.py
from mat.show_version import get_show_version

all_cdp_data = [ 
    sw1_show_cdp_neighbors_detail,
    r1_show_cdp_neighbors_detail,
    r2_show_cdp_neighbors_detail,
    r3_show_cdp_neighbors_detail,
    r4_show_cdp_neighbors_detail,
    r5_show_cdp_neighbors_detail,
]


# initialize dict
network_devices = {}

count = 0
for cdp_detail in all_cdp_data:

    # each entry is separated by long ----....- 
    cdp_detail_split = cdp_detail.split('-------------------------')

    for d in cdp_detail_split:
        # make sure we process long lists of nothing
        d = d.strip()

        device = ''
        for line in d.splitlines():
            line = line.strip()
            # try to parse for show version
            #pprint ( detail)
            #pprint ( get_show_version( line ))    

            if "Device ID:" in line:
                # split line against ":", device id is the last one
                device = line.split(":")[-1].strip()
                network_devices [ device ] = {}

            elif "IP address:" in line:
                # split line against ":", ip is the last one
                ip = line.split(":")[-1].strip()
                network_devices [ device ]['ip'] = ip
            
            elif "Platform:" in line:
                # first split with "," and take 1st element
                platform, capabilities = line.split(",")

                # split platform against ":", model is the last one
                model = platform.split(":")[-1].strip()
                network_devices [ device ]['model'] = model

                # split line against ":", device_type is the last one
                device_type = capabilities.split(":")[-1].strip()
                network_devices [ device ]['device_type'] = device_type
            else:
                pass
                #print "WTF"

        if device:
            network_devices [ device ][ 'vendor' ] = get_show_version(d)['vendor']
            # initialize the list of neighbours
            network_devices [ device ]['adjacent_devices'] = []


cdp_topology = {
    'SW1':  sw1_show_cdp_neighbors,
    'R1':   r1_show_cdp_neighbors,
    'R2':   r2_show_cdp_neighbors,
    'R3':   r3_show_cdp_neighbors,
    'R4':   r4_show_cdp_neighbors,
    'R5':   r5_show_cdp_neighbors,
    }

for host,cdp_data in cdp_topology.items():

    # setup a flag to allow us parse only neighbour lines correctly
    next_lines_are_neighbours = False
    for line in cdp_data.splitlines():
        line = line.strip()

        if not line :
            continue
       
        # look for Device ID, next lines should be topology information
        if 'Device ID' in line:
            next_lines_are_neighbours = True
            continue

        if next_lines_are_neighbours:
            line = line.split()
            network_devices [ host ]['adjacent_devices'].append (line[0])
            


pprint ( network_devices )
