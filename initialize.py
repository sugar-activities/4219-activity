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

import string
import os
import sys
class initialize:
    rec_line = []    
    def _init_(self,file_name):
        self.file_name = file_name
        
    def get_data():
        file_dat = open(file_name,'r')
        dat_lines = file_dat.readlines()
        file_dat.close()
        for each_line in dat_lines:
            length = len(each_line) - 1
            if each_line[0] == '\n' or each_line[0] == '#':
                continue
            else:
                rec_line.append(each_line[0:length])
            
    def ini_val_facility():
        COST_HOUSE = {rec_line[0] : float(rec_line[1]),rec_line[2] : float(rec_line[3]),rec_line[4] : float(rec_line[5]}  

def init_val():
    global COST_HOUSE
    init_obj = initialize("initial.ini")
    init_obj.get_data()
    init_obj.ini_val_facility()
    print COST_HOUSE

def main():
    init_val()

if __name__ == "__main__" :
    main()
