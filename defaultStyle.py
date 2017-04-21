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
import os
from gettext import gettext as _

def init(gui):
    #Surface Loading
    buttonsurf = pygame.image.load(os.path.join('art','button.png')).convert_alpha()
    closesurf = pygame.image.load(os.path.join('art','closebutton.png')).convert_alpha()
    shadesurf = pygame.image.load(os.path.join('art','shadebutton.png')).convert_alpha()
    checksurf = pygame.image.load(os.path.join('art','checkbox.png')).convert_alpha()
    optionsurf = pygame.image.load(os.path.join('art','optionbox.png')).convert_alpha()
    combosurf = pygame.image.load(os.path.join('art','combobox.png')).convert_alpha()
    
    #Default gui font
    gui.defaultFont = pygame.font.Font("font.ttf", 12)
    
    #Label Style
    gui.defaultLabelStyle = {'font-color': (255,255,255),
                          'font': gui.defaultFont,
                          'bg-color': (0,0,0),
                          'autosize': False,
                          "antialias": True,
                          'border-width': 0,
                          'border-color': (255,255,255),
                          'wordwrap': True}
    
    #Button style
    gui.defaultButtonStyle = gui.createButtonStyle(gui.defaultFont, (0,0,0), buttonsurf,4,1,4,4,1,4,4,1,4,4,1,4)
    
    #Close button style
    closeButtonStyle = gui.createImageButtonStyle(closesurf, 20)
    
    #Close button style
    shadeButtonStyle = gui.createImageButtonStyle(shadesurf, 20)
    
    #Window style
    gui.defaultWindowStyle = {'font': gui.defaultFont,
                            'font-color': (255,255,255),
                            'bg-color' : (0,0,0,100),
                            'shaded-font-color': (255,200,0),
                            'shaded-bg-color' : (100,0,0,100),
                            'border-width': 1,
                            'border-color': (150,150,150, 255),
                            'offset': (5,5),
                            'close-button-style': closeButtonStyle,
                            'shade-button-style': shadeButtonStyle
                            }
    
    #TextBox style
    gui.defaultTextBoxStyle = {'font': gui.defaultFont,
                               'font-color':(255,255,255),
                               'bg-color-normal':(55,55,55),
                               'bg-color-focus': (70,70,80),
                               'border-color-normal': (0,0,0),
                               'border-color-focus': (0,50,50),
                               'border-width': 1,
                               'appearence': gui.APP_3D,
                               'antialias': True,
                               'offset':(4,4)}
    
    #CheckBox style
    gui.defaultCheckBoxStyle = gui.createCheckBoxStyle(gui.defaultFont, checksurf, 12, (255,255,255),
                                                       (100,100,100), autosize = True)
    
    #Optionbox style
    gui.defaultOptionBoxStyle = gui.createOptionBoxStyle(gui.defaultFont, optionsurf, 12, (255,255,255),
                                                     (100,100,100), autosize = True)
    
    #ListBox style
    gui.defaultListBoxStyle = {'font': gui.defaultFont,
                               'font-color': (255,255,255),
                               'font-color-selected': (0,0,0),
                               'bg-color': (55,55,55),
                               'bg-color-selected': (160,180,200),
                               'bg-color-over': (60,70,80),
                               'border-width': 1,
                               'border-color': (0,0,0),
                               'item-height': 18,
                               'padding': 2,
                               'autosize': False}
    
    #ComboBox style
    gui.defaultComboBoxStyle = gui.createComboBoxStyle(gui.defaultFont, combosurf, 15, (255,255,255),
                                                       borderwidth = 1, bordercolor = (31,52,78),
                                                       bgcolor = (55,55,55))
    
