#!/usr/bin/env python
# Class 5 
# Exercise 1 
# Author Mateusz Blaszczyk


print "Class 5, Exercise 1"

""" Parse the CDP data (see link above) to obtain the following information:
hostname, ip, model, vendor, and device_type
(device_type will be either 'router', 'switch', or 'unknown').

From this data create a dictionary of all the network devices.


The network_devices dictionary should have the following format:

network_devices = {
    'SW1': { 'ip': '10.1.1.22', 'model': 'WS-C2950-24', 'vendor': 'cisco', 'device_type': 'switch' },
    'R1': { 'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router' },
    ...
    'R5': { 'ip': '10.1.1.1', 'model': '881', 'vendor': 'Cisco', 'device_type': 'router' },
}
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

pprint ( network_devices )
