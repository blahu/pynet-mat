#!/usr/bin/env python
# Class 5
# Exercise 2
# Author mat
"""
2. Using Arista's eapilib, create a script that allows you to add a VLAN (both
the VLAN ID and the VLAN name).  Your script should first check that the VLAN
ID is available and only add the VLAN if it doesn't already exist.  Use VLAN
IDs between 100 and 999.  You should be able to call the script from the
command line as follows:
    python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.
    python eapi_vlan.py --remove 100          # remove VLAN100

Once again only remove the VLAN if it exists on the switch.  You will probably
want to use Python's argparse to accomplish the argument processing.
"""
__author__ = 'mateusz'

from eapilib import create_connection
from pprint import pprint

class AristaSwitch:
    """
    Abstraction fro Arista EAPI calls:
    """

    def __init__(self, **params):
        """ 
        this function initializes the EAPI calls:
        """
        self.sw = create_connection( **params )

    def check_vlan_exists ( self, vlan_id ):
        """
        this function should say yes/no if vlan id exists
        but
        it returns name if exists
        or False if not
        """
        # run command on a switch 
        resp = self.sw.run_commands ( ['show vlan'] )

        # decapsulate from external list
        resp =  resp [0]

        for v in resp['vlans'].keys():
            try:
                if int(v) == int(vlan_id):
                    # found vlan
                    return resp['vlans'][v]['name']

            except ValueError as e:
                raise e
        return False

    def show_vlans ( self ):
        """
        this function should just output/print all vlans on switch
        """
        # run command on a switch 
        resp = self.sw.run_commands ( ['show vlan'] )

        # decapsulate from external list
        resp =  resp [0]

        pprint(resp['vlans'])
        return True

    def add_vlan ( self, vlan_id, vlan_name ):
        """
        this function should add a vlan
        """
        commands = [ "vlan {}".format (vlan_id) , "name {}".format (vlan_name) ]
        resp = self.sw.config ( commands )
        return True

    def del_vlan ( self, vlan_id ):
        """
        this function should delete a vlan
        """
        commands = [ "no vlan {}".format (vlan_id) ]
        resp = self.sw.config ( commands )
        return True


if __name__ == '__main__':
    params =  { 'username': 'eapi', 'password': 'eapu', 'hostname': '10.1.1.3' }
    sw = AristaSwitch(**params)
    
    def add ( args ):
        #add a vlan, if not exists
        name = sw.check_vlan_exists (args.vlan)
        if name is False:
            sw.add_vlan(args.vlan, args.name)
    
    def rem ( args ):
        #delete a vlan
        sw.del_vlan(args.vlan)
    #
    def show ( args):
        #print all vlans
        sw.show_vlans()

    # if executed from command line we would like to parse few args:
    import argparse
    parser = argparse.ArgumentParser(description="Add or remove vlans from Arista switch")
    subparsers = parser.add_subparsers()

    # add parser
    parser_add = subparsers.add_parser('add')
    parser_add.add_argument("name")
    parser_add.add_argument("vlan", type=int)
    parser_add.set_defaults (func=add)

    # del parser
    parser_add = subparsers.add_parser('rem')
    parser_add.add_argument("vlan", type=int)
    parser_add.set_defaults (func=rem)

    # print parser
    parser_add = subparsers.add_parser('show')
    parser_add.set_defaults (func=show)

    args = parser.parse_args()
    args.func(args)

