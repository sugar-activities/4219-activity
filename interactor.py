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

from  threades import *

class interactor:
    '''Class meant for implementing the interaction messages'''
    def  check_all(self):
        self.check_food()
        self.check_money()
        self.check_
