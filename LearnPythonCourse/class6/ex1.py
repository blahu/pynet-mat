#!/usr/bin/env python
"""
Class 6
Exercise 1
Author Mat
"""

"""
1. Create a function that returns the multiplication product of three parameters (x, y, z).  
z should have a default value of 1.
a. Call the function with all positional arguments.
b. Call the function with all named arguments.  
c. Call the function with a mix of positional and named arguments.
d. Call the function with only two arguments and use the default value for z.
"""


def f1 (x, y, z=1):
    '''
    function that returns the multiplication product of three parameters
    (x, y, z)
    z should have a default value of 1.
    '''
    return x*y*z

print "a:" +  str ( f1 (2,3,4) )
print "b:" +  str ( f1 (x=2,y=3,z=4) )
print "c:" +  str ( f1 (2,z=3,y=4) )
print "d:" +  str ( f1 (2,y=3) )


