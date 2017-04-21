#! /usr/bin/env python
#
# Food Force II code module of the Food Force II package
#
# (c) Copyright 2009 Software for Education, Entertainment and Training Activities (http://seeta.in)
# The contents of this file are subject to the Artistic License 2.0; you may not
# use this file except in compliance with the License. 
# Some of the other files in the Food Force II package are licensed under
# different licenses. Please note the licenses of the modules you use.
#
# Code History:
#
# Food Force II activity beta-version was released on May 8, 2009 with great success - http://blog.laptop.org/2009/05/08/food-force-2-makes-waves/.
# The activity was forked into separate projects on June 23.
# One will be maintained and developed under the aegis of SEETA - http://seeta.in/j/products-and-services/food-force-ii.html.
# And, the other would be developed and maintained by Mohit Taneja and Deepank Gupta, who worked on developing the code of this learning activity till 
# the beta release, and were recommended to Walter Bender by Manusheel Gupta to work on this project with him in 2008.
#
# The lead developer of this project is Vijit Singh, who is working with developers Nitish Goyal and Yogesh Garg to develop Food Force II
# with Manusheel Gupta. 
# For feedback or questions please contact us at foodforce2@seeta.in. 




# Macros or say global variables for all the type of events in the game
BUILDFACILITYEVENT = 1
UPGRADEFACILITYEVENT = 2
STOPFACILITYEVENT = 3
RESUMEFACILITYEVENT = 4
DEMOLISHFACILITYEVENT = 5
BUYRESOURCESEVENT = 6
SELLRESOURCESEVENT = 7
ACTIONCOMPLETEEVENT = 8



class eventsQueue:
    ''' The class which will maintain a queue of all the game events
    '''
    
    queue = []
    def add(self,event):
        ''' Adds an event to the queue
        '''
        self.queue.append(event)
        
    def pop(self):
        ''' Pops an event from the queue
        '''
        val = self.queue.pop()
        return val
    
    def get_events(self):
        ''' Sends all the events in the event queue
            also empties the event queue
        '''
        val = self.queue
        self.queue = []
        return val
    
# Initialising an object of the events queue class
EventQueue = eventsQueue()

class Event:
    ''' Generic class for events, each event in 
        the event queue should be an object of this class 
    '''
    
    type = 0
    facility_name = ''
    res_name = ''
    res_quantity = 0
    
    def __init__(self, type = 0, facility_name = '', res_name = '' , res_quantity = 0):
        ''' Initialises the quantity of various variables
        '''
        
        self.type = type
        self.res_name = res_name
        self.facility_name = facility_name
        self.res_quantity = res_quantity
        
        
