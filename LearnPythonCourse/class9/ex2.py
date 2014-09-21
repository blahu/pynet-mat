#!/usr/bin/env python
"""
Class 9
Exercise 2
Author mateusz

II. Create an Uptime class that takes in a Cisco IOS uptime string and parses
the string into years, weeks, days, hours, minutes (assigning these as
attributes of the object).
"""
__author__ = 'mateusz'

class Uptime(object):
    """
    class that takes in a Cisco IOS uptime string and parsesthe string into
    years, weeks, days, hours, minutes
    """
    def __init__(self, string):
        self.full_string = string
        
        string_splitted = string.split(' uptime is ')
        self.hostname = string_splitted [0]
        self.fulltime= string_splitted [1]
        self.uptime_list = self.fulltime.split(r',')
        self.years = 0
        self.weeks = 0
        self.days = 0
        self.hours = 0
        self.minutes = 0

    def parse(self):
        """
        parses the string into years, weeks, days, hours, minutes 
        """
        period_list = ['year', 'week', 'day', 'hour', 'minute']
        attr_list   = [0,0,0,0,0]
        
        for t in self.uptime_list:

            for i in range(len(period_list)):

                if period_list[i] in t:

                    # first strip leading spaces, then take first non space part as the number
                    string_value = t.strip().split(r' ')[0]
                    try:
                        attr_list[i] = int(string_value)
                    except ValueError as e:
                        print ("ERROR:{} for int({})".format(e, string_value))

                    #print ("t={}, i={}, period_list={} attr_list={}".format(t,i,period_list[i],attr_list[i]))
                    continue

        self.years,self.weeks,self.days,self.hours,self.minutes = attr_list




if __name__ == '__main__':
    # tests
    test_obj = Uptime('twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes')

    print ("Test1: hostname= {}".format(test_obj.hostname))
    print ("Test2: fulltime= {}".format(test_obj.fulltime))
    print ("Test3: up_list = {}".format(test_obj.uptime_list))

    test_obj.parse()

    print ("Test4a: years   = {}".format(test_obj.years))
    print ("Test4b: weeks   = {}".format(test_obj.weeks))
    print ("Test4c: days    = {}".format(test_obj.days))
    print ("Test4d: hours   = {}".format(test_obj.hours))
    print ("Test4e: minutes = {}".format(test_obj.minutes))
