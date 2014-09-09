#!/usr/bin/env python

# show version, def'ed from class4/ex2
# https://github.com/blahu/pynet-mat/blob/master/class4/ex2.py


def get_show_version(show_version_data):
    """ 
    get unparsed cisco show version 
    @returns dictionary of
      - vendor
      - os_version
      - model
      - serial_number
      - uptime
    """
    dictionary = {}
    for line in show_version_data.splitlines():
        
        # First look for version - collect vendor and version
        if 'IOS ' in line:
            # must be cisco!
            dictionary ['vendor'] = "Cisco"
            
            # split line with comma
            line_split = line.split(',')

            # os_version is 2nd to last element 'Version 15.0(1)M4'
            # end 2nd element of that is 15... - os_version
            dictionary ['os_version'] = line_split[-2].split()[1]
        
        elif 'bytes of memory' in line:
            # split line with space
            line_split = line.split()
            
            # 2nd element is model
            dictionary ['model'] = line_split[1]
        
        elif 'Processor board ID' in line:
            # split line with space
            line_split = line.split()
            
            # last element is the Serial No
            dictionary ['serial_number'] = line_split[-1]

        elif 'uptime is' in line:
            # split line with space but only the first 3
            line_split = line.split (' ', 3)
            
            # last (3rd) element is the uptime
            dictionary ['uptime'] = line_split[3]

    return dictionary
