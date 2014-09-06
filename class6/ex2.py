#!/usr/bin/env python
"""
Class 6
Exercise 2
Author Mat
"""

"""
2. Write a function that converts a list to a dictionary where the index of the list is used as the key to the new dictionary (the function should return the new dictionary).
"""


def list_to_dict (a_list):
    a_dict = {}
    for e in enumerate (a_list, 1):
        a_dict[ e[0] ] = e[1]
    return a_dict


a = range (4)

from pprint import pprint

pprint ( a )
pprint ( list_to_dict(a) )
