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
        self.parse ()

    def parse(self):
        """
        parses the string into years, weeks, days, hours, minutes 
        """
        period_list = ['year', 'week', 'day', 'hour', 'minute']
        values_list = [0,0,0,0,0]
        
        for t in self.uptime_list:

            for i in range(len(period_list)):

                if period_list[i] in t:

                    # first strip leading spaces, then take first non space part as the number
                    string_value = t.strip().split(r' ')[0]
                    try:
                        values_list[i] = int(string_value)
                    except ValueError as e:
                        print ("ERROR:{} for int({})".format(e, string_value))

                    continue

        self.years,self.weeks,self.days,self.hours,self.minutes = values_list




if __name__ == '__main__':
    # tests
    DEBUG=False
    tests = {
            'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes' :(0, 6, 4, 2,25),
            '3750RJ uptime is 1 hour, 29 minutes'                       :(0, 0, 0, 1,29),
            'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'  :(0, 8, 4,18,16),
            'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'     :(5,18, 0, 8,23),
    }
    for test_string,test_result in tests.items():
        test_obj = Uptime(test_string)

        if DEBUG:
            print ("Test1: hostname= {}".format(test_obj.hostname))
            print ("Test2: fulltime= {}".format(test_obj.fulltime))
            print ("Test3: up_list = {}".format(test_obj.uptime_list))
            print ("Test4a: years   = {}".format(test_obj.years))
            print ("Test4b: weeks   = {}".format(test_obj.weeks))
            print ("Test4c: days    = {}".format(test_obj.days))
            print ("Test4d: hours   = {}".format(test_obj.hours))
            print ("Test4e: minutes = {}".format(test_obj.minutes))

        result = ( test_obj.years,test_obj.weeks,test_obj.days,test_obj.hours,test_obj.minutes)

        if result == test_result:
            result_text = 'ok'
        else:
            result_text = 'failed, was {} should be {}'.format (result, test_result)

        print "{:.<80}{}".format (test_string + ' ', result_text)

