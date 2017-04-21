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

import pygame
from pygame.locals import *
from sys import exit
import os
from time import *
import threades
import threading
import game_events
import texts
import model
import gui_buttons
import random
from gettext import gettext as _



class Earthquake(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        mask= pygame.surface.Surface((1200,560),SRCALPHA)
        mask.fill((0,0,0))
        mask.set_alpha(0)
        self.alpha = 0
        self.image = mask
        self.rect = self.image.get_rect()
        self.rect.move((0,0))
        self.counter = 0
        self.prev_disp = (0,0)
        self.move_dir = [(-20,-20),(-20,-10),(-20,0),(-20,10),(-20,20),(-10,-20),(-10,-20),(-10,0),(-10,10),(-10,20),(0,-20),(0,-10),(0,0),(0,10),(0,20),(10,-20),(10,-20),(10,0),(10,10),(10,20),(20,-20),(20,-10),(20,0),(20,10),(20,20)]
        # To close all open windows
        if gui_buttons.gui_obj.get_child_win_flag():
            gui_buttons.gui_obj.close_child_win()
            gui_buttons.gui_obj.close_win()
        elif gui_buttons.gui_obj.get_win_flag():
            gui_buttons.gui_obj.close_win()

    def update(self):

        global Hospital
        global House
        global School
        global Workshop
        global ppl


        self.counter +=1
        if self.counter <50:
            threades.transform_obj.move_free((-self.prev_disp[0],-self.prev_disp[1]))
            self.prev_disp = self.move_dir[int(random.random()*25)]
            threades.transform_obj.move_free(self.prev_disp)
        if self.counter >20 and self.counter <50:
            self.alpha +=8
            self.image.set_alpha(self.alpha)
        if self.counter==40:
            display_text = _(' Your Village Sheylan has ben hit by an Earthquake')
            threades.message.push_message(display_text,'high')
        if self.counter == 80:
            display_earthquake_images()
            threades.demolish_facility('Hospital')
            threades.demolish_facility('House')
            threades.demolish_facility('House')
            threades.demolish_facility('House')
            threades.demolish_facility('School')
            threades.demolish_facility('Workshop')
            model.ppl.change_total_population(-10)
        if self.counter > 81:
            if self.alpha >2:
                self.alpha -=2
            self.image.set_alpha(self.alpha)
        if self.counter >180:
            event = game_events.Event(type = game_events.ACTIONCOMPLETEEVENT, facility_name = '', res_name = '' , res_quantity = 0)
            game_events.EventQueue.add(event)
            threades.natural_calamities.remove(earthquake)

def display_earthquake_images():

    image1 = pygame.image.load(os.path.join('data', 'earthquake1.png')).convert()
    threades.screen.blit(pygame.transform.scale(image1,threades.new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)

    image2 = pygame.image.load(os.path.join('data', 'earthquake2.png')).convert()
    threades.screen.blit(pygame.transform.scale(image2,threades.new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)

    image3 = pygame.image.load(os.path.join('data', 'earthquake3.png')).convert()
    threades.screen.blit(pygame.transform.scale(image3,threades.new_screen_size),(0,0))
    pygame.display.flip()
    sleep(3)
    
earthquake = None

def earthquake():
    ''' This method needs to be called when there is an earthquake in the
    village, it decreases the number of installations of some facilities and
    also reduce the population
    '''
    global earthquake

    earthquake  = Earthquake()
    threades.natural_calamities.add(earthquake)
