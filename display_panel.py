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


from sys import exit
import os
from time import *
#from threades import *
import threades
import threading

import gui
#from gui import *
#from gui_buttons import *
import gui_buttons
import model
#from model import *
import pygame
import load_images
from gettext import gettext as _
from olpcgames import pangofont

class bar:

    color_bar = (47,47,255)

    def __init__(self, (x_value, y_value)):
        ''' Draws a bar on the surface at posn x,y
        '''
        self.x = x_value
        self.y = y_value

        pygame.draw.rect(threades.screen,self.color_bar,threades.resize_rect((self.x,self.y,250,18)),2)

        pygame.draw.rect(threades.screen,(255,255,255),threades.resize_rect((self.x+2,self.y+2,246,14)))



    def update_value(self,value):
        '''Updates the value of the bar
        '''

        max_value = 100.0
        max_pixel = 246.0
        colour = (177,135,73)           
        pygame.draw.rect(threades.screen,self.color_bar,threades.resize_rect((self.x,self.y,250,18)),2)        
        pygame.draw.rect(threades.screen,colour,threades.resize_rect((self.x+2,self.y+2,value/max_value*max_pixel,14)))
        pygame.draw.rect(threades.screen,(255,255,255),threades.resize_rect((self.x+2+value/max_value*max_pixel,self.y+2,max_pixel-value/max_value*max_pixel,14)))







class indicator_panel:

    ##global threades.desktop
    font_bg_color = (0,0,0)       # This should be same as  the background colour for the label
    font_color = (255,214,150)    # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the indicator panel on the surface
        '''
        
        self.update_flag = True

        myfont1 = pangofont.PangoFont(size=threades.resize_pt(30))   # For main heading

        myfont2 = pangofont.PangoFont(size=threades.resize_pt(25))   # For indicators name
        myfont3 = pangofont.PangoFont(size=threades.resize_pt(16),bold=True)
        # Creating a custom label style
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 1
        self.labelstyle1['wordwrap'] = True
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        self.labelstyle1['border-color'] = self.color_grey
        # Drawing main Indicator label
        label = gui.Label(position = threades.resize_pos((900,600)),size = threades.resize_pos((300,45)), parent = threades.desktop, text = "      "+_("Indicators"), style = self.labelstyle1)

        #print " deawing indicator panel"
        
        # Creating second custom label
        self.labelstyle2 = gui.defaultLabelStyle.copy()
        self.labelstyle2['border-width'] = 0
        self.labelstyle2['wordwrap'] = True
        self.labelstyle2['autosize'] = False
        self.labelstyle2['font'] = myfont2
        self.labelstyle2['font-color'] = self.font_color
        self.labelstyle2['border-color'] = self.color_grey
        # Drawing all the indicators
        ind_namelist = (_(' Housing'),_(' Nutrition'),_(' Health'),_(' Education'),_(' Training'))

        # Creating second custom label
        self.labelstyle3 = gui.defaultLabelStyle.copy()
        self.labelstyle3['border-width'] = 0
        self.labelstyle3['wordwrap'] = False
        self.labelstyle3['autosize'] = True
        self.labelstyle3['font'] = myfont3
        self.labelstyle3['font-color'] = self.font_color
        self.labelstyle3['border-color'] = self.color_grey
        
        # Empty Dictionary for bar
        self.bar_dict = []
        name_label_size = threades.resize_pos((300,25))
        self.value_labels = []
        for i in range(5):
            label = gui.Label(position = threades.resize_pos((900,650+50*i)),size = name_label_size, parent = threades.desktop, text = ind_namelist[i], style = self.labelstyle2)
            self.bar_dict.append(bar((902,677+50*i)))
            label = gui.Label(position = threades.resize_pos((1160,677+50*i)), parent = threades.desktop, text = str(0), style = self.labelstyle3)
            self.value_labels.append(label)
    




    def update_value(self):
        ''' Updates the values of all the indicators
        '''
        
        for i in range(5):

            self.bar_dict[i].update_value(model.indicators_list[i].get_value())
            if not (self.value_labels[i].text == str(int(model.indicators_list[i].get_value()))+'%'):
                self.update_flag = True
                
        #print 'update flag is',self.update_flag,'panel flag is',threades.panel_update_flag,'total is',threades.total_update_flag
        
        if self.update_flag or threades.panel_update_flag or threades.total_update_flag:
            pygame.draw.line(threades.screen,self.color_grey,threades.resize_pos((900,645)),threades.resize_pos((900,900)),1)
        
            for i in range(5):
    
                self.bar_dict[i].update_value(model.indicators_list[i].get_value())
                if not (self.value_labels[i].text == str(int(model.indicators_list[i].get_value()))+'%'):
                    self.value_labels[i].text = str(int(model.indicators_list[i].get_value()))+'%'

        self.update_flag = False
        




class resources_panel:


    ##global threades.desktop
    font_bg_color = (0,0,0)             # This should be same as  the background colour for the label
    font_color = (255,214,150)      # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the model.resources panel on the surface
        '''
        
        self.update_flag = True
        self.money_flag = True
        self.time_flag = False
        self.time_help_value=0
        myfont1 = pangofont.PangoFont(size=threades.resize_pt(30))   # For main heading
        myfont2 = pangofont.PangoFont(size=threades.resize_pt(25))   # For model.resources name and their value
        myfont3 = pangofont.PangoFont(size=threades.resize_pt(16))
        myfont4 = pangofont.PangoFont(size=threades.resize_pt(18))   # For the display of model.money
        
        # Creating a custom label style
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 1
        self.labelstyle1['wordwrap'] = True
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        self.labelstyle1['border-color'] = self.color_grey
        

        # Drawing main Resources rectangle
        label = gui.Label(position = threades.resize_pos((400,600)),size = threades.resize_pos((500,45)), parent = threades.desktop, text = "                    "+_("Resources"), style = self.labelstyle1)

        # Creating second label style
        self.labelstyle2 = gui.defaultLabelStyle.copy()
        self.labelstyle2['border-width'] = 0
        self.labelstyle2['wordwrap'] = True
        self.labelstyle2['autosize'] = False
        self.labelstyle2['font'] = myfont2
        self.labelstyle2['font-color'] = self.font_color
        
        self.labelstyle3 = gui.defaultLabelStyle.copy()
        self.labelstyle3['border-width'] = 0
        self.labelstyle3['wordwrap'] = False
        self.labelstyle3['autosize'] = True
        self.labelstyle3['font'] = myfont3
        self.labelstyle3['font-color'] = self.font_color
        
        self.labelstyle4 = gui.defaultLabelStyle.copy()
        self.labelstyle4['border-width'] = 0
        self.labelstyle4['wordwrap'] = False
        self.labelstyle4['autosize'] = True
        self.labelstyle4['font'] = myfont4
        self.labelstyle4['font-color'] = (160,160,160)
        self.money_label = gui.Label(position = threades.resize_pos((850,10)), parent = threades.desktop, text = _('Money -:')+'   '+str(int(model.money.get_money()))+'      ', style = self.labelstyle4)
        self.time_label= gui.Label(position = threades.resize_pos((300,10)), parent = threades.desktop, text = _('Time Elapsed -:')+'   '+_('Level Just Started')+'      ', style = self.labelstyle4)
        self.value_labels = []
        # Drawing general model.resources list
        list_gen_res = (_(' Water'),_(' Building Materials'),_(' Tools'),_(' Medicines'),_(' Books'))
        for i in range(5):
            label = gui.Label(position = threades.resize_pos((400,645+35*i)),size = threades.resize_pos((200,35)), parent = threades.desktop, text = list_gen_res[i], style = self.labelstyle2)
            label = gui.Label(position = threades.resize_pos((605,649+35*i)), parent = threades.desktop, text = str(int(model.resources[i].get_vquantity())), style = self.labelstyle3)
            self.value_labels.append(label)
            
        # Drawing food model.resources list
        list_food_res = (_(' Rice'),_(' Fruit & Vegatables'),_(' Beans'),_(' Sugar'),_(' Salt'),_(' Oil'))
        for i in range(6):
            label = gui.Label(position = threades.resize_pos((650,645+35*i)),size = threades.resize_pos((200,35)), parent = threades.desktop, text = list_food_res[i], style = self.labelstyle2)
            label = gui.Label(position = threades.resize_pos((855,649+35*i)), parent = threades.desktop, text = str(int(model.resources[i+5].get_vquantity())), style = self.labelstyle3)
            self.value_labels.append(label)
    

    def update_value(self):
        ''' Updates the model.resources panel
        '''

        self.money_flag = False
        for i in range(11):
            if not (self.value_labels[i].text == str(int(model.resources[i].get_vquantity()))):
                self.update_flag = True
        
        if self.update_flag or threades.panel_update_flag or threades.total_update_flag:
           
            
            pygame.draw.line(threades.screen,self.color_grey,threades.resize_pos((400,645)),threades.resize_pos((400,855)),1)
            pygame.draw.line(threades.screen,self.color_grey,threades.resize_pos((650,645)),threades.resize_pos((650,855)),1)
    
            for i in range(11):
                if not (self.value_labels[i].text == str(int(model.resources[i].get_vquantity()))):
                    self.value_labels[i].text = str(int(model.resources[i].get_vquantity()))
        
        if not (self.money_label.text == _('Money -:   ')+str(int(model.money.get_money()))+'      '):
            self.money_flag = True
            self.money_label.text = _('Money -:   ')+str(int(model.money.get_money()))+'      '
         
        #print 'no of days is',model.game_controller.get_days()
        if self.time_flag==True:
            #self.time_label.text=''
            #NOTE: Here, I am not adding as if years is not 0 , then only it will be blitted becoz if do like that the things will keep on changing, not a nice view
            self.time_label.text=_('Time Elapsed -:   ')+_('Years: ')+str(model.game_controller.get_years())+_('  Months: ')+str(model.game_controller.get_months()) +_('  Days: ')+str(model.game_controller.get_days()) 
            self.time_flag=False
            
        #to update the money flag
        
        #print 'global_time is',model.game_controller.get_global_time(),'while the time_help_value is',self.time_help_value
        if (model.game_controller.get_global_time()>((model.game_controller.conversion_factor)+self.time_help_value)):
            self.time_flag=True
            self.time_help_value=model.game_controller.get_global_time()
            
            
        self.update_flag = False
        
    
    
    


class manpower_panel:

    ##global threades.desktop
    font_bg_color = (0,0,0)       # This should be same as  the background colour for the label
    font_color = (255,214,150)    # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the manpower panel
        '''
        
        self.update_flag = True
        myfont1 = pangofont.PangoFont(size=threades.resize_pt(30))   # For main heading
        myfont2 = pangofont.PangoFont(size=threades.resize_pt(25))   # For model.resources name and their value
        myfont3 = pangofont.PangoFont(size=threades.resize_pt(25))   # For model.resources name and their value

        # Creating a custom label style
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 1
        self.labelstyle1['wordwrap'] = True
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        self.labelstyle1['border-color'] = self.color_grey

        # Drawing main Manpower Resources rectangle
        label = gui.Label(position = threades.resize_pos((0,600)),size = threades.resize_pos((400,45)), parent = threades.desktop, text = _("  Manpower Distribution"), style = self.labelstyle1)

        # Creating second label style
        self.labelstyle2 = gui.defaultLabelStyle.copy()
        self.labelstyle2['border-width'] = 0
        self.labelstyle2['wordwrap'] = True
        self.labelstyle2['autosize'] = False
        self.labelstyle2['font'] = myfont2
        self.labelstyle2['font-color'] = self.font_color
        self.labelstyle2['border-color'] = self.color_grey

        self.labelstyle3 = gui.defaultLabelStyle.copy()
        self.labelstyle3['border-width'] = 0
        self.labelstyle3['wordwrap'] = False
        self.labelstyle3['autosize'] = True
        self.labelstyle3['font'] = myfont3
        self.labelstyle3['font-color'] = self.font_color
        self.labelstyle3['border-color'] = self.color_grey

        # Drawing Manpower model.resources list
        list_names = (_(' Total Population'),_(' Sheltered People'),_(' Educated People'),_(' Healthy People'),_(' People Fed'),_(' People Employed'))
        list_values = (model.ppl.get_total_population(),model.ppl.get_no_of_ppl_sheltered(),model.ppl.get_no_of_ppl_educated(),model.ppl.get_no_of_ppl_healthy(),model.ppl.get_no_of_ppl_fed(),model.ppl.get_total_no_of_ppl_emp())
        
        self.value_labels = []
        for i in range(6):
            label = gui.Label(position = threades.resize_pos((0,645+35*i)),size = threades.resize_pos((350,35)), parent = threades.desktop, text = list_names[i], style = self.labelstyle2)
            label = gui.Label(position = threades.resize_pos((355,649+35*i)), parent = threades.desktop, text = str(int(list_values[i])), style = self.labelstyle3)
            self.value_labels.append(label)


    def update_value(self):
        ''' Updates the Manpower panel
        '''
        list_values = (model.ppl.get_total_population(),model.ppl.get_no_of_ppl_sheltered(),model.ppl.get_no_of_ppl_educated(),model.ppl.get_no_of_ppl_healthy(),model.ppl.get_no_of_ppl_fed(),model.ppl.get_total_no_of_ppl_emp())
        for i in range(6):

            if not (self.value_labels[i].text == str(int(list_values[i]))):
                self.update_flag = True
        
        if self.update_flag or threades.panel_update_flag or threades.total_update_flag:

            pygame.draw.line(threades.screen,self.color_grey,threades.resize_pos((900,645)),threades.resize_pos((900,855)),1)
            pygame.draw.rect(threades.screen,self.color_grey,threades.resize_rect((0,855,300,45)),2)        
            pygame.draw.rect(threades.screen,self.color_grey,threades.resize_rect((300,855,300,45)),2)        
            pygame.draw.rect(threades.screen,self.color_grey,threades.resize_rect((600,855,300,45)),2)        
    
            for i in range(6):
    
                if not (self.value_labels[i].text == str(int(list_values[i]))):
                    self.value_labels[i].text = str(int(list_values[i]))
        
        self.update_flag = False
        
    
class facilities_panel:

    #global threades.desktop
    font_bg_color = (255,255,255)       # This should be same as  the background colour for the label
    font_color = (255,214,150)    # This should be same as that for the font to be written on the label
    color_grey = (160,160,160)
    def __init__(self):
        ''' Draws the Facilities panel
        '''
        self.update_flag = True
        myfont1 = pangofont.PangoFont(size=threades.resize_pt(25))   # For model.resources name and their value
        
        self.labelstyle1 = gui.defaultLabelStyle.copy()
        self.labelstyle1['border-width'] = 0
        self.labelstyle1['wordwrap'] = False
        self.labelstyle1['autosize'] = False
        self.labelstyle1['font'] = myfont1
        self.labelstyle1['font-color'] = self.font_color
        #self.labelstyle1['bg-color'] = self.font_bg_color
        
        self.list_titles = (_('Houses '),_('Schools '),_('Hospitals '),_('Workshops '),_('Farms '),_('Wells '))
        self.list_names = (_('Number: '),_('Number: '),_('Number: '),_('Number: '),_('Number: '),_('Number: '))
        self.list_values1 = (model.House.get_number(),model.School.get_number(),model.Hospital.get_number(),model.Workshop.get_number(),model.Farm.get_number(),model.Fountain.get_number())
        self.list_values2 = (model.House.get_level(),model.School.get_level(),model.Hospital.get_level(),model.Workshop.get_level(),model.Farm.get_level(),model.Fountain.get_level())
        self.value_labels = []
        for i in range(6):
            label = gui.Label(position = threades.resize_pos((950,50+55*i)),size = threades.resize_pos((300,30)), parent = threades.desktop, text = self.list_titles[i], style = self.labelstyle1)
            label = gui.Label(position = threades.resize_pos((950,75+55*i)),size = threades.resize_pos((300,30)), parent = threades.desktop, text = self.list_names[i]+str(int(self.list_values1[i]))+_(' Level: ')+str(int(self.list_values2[i])), style = self.labelstyle1)
            label.surf.set_alpha(200)
            self.value_labels.append(label)


    def update_value(self):
        ''' Updates the Facilities panel
        '''
        for i in range(6):

            if not (self.value_labels[i].text == self.list_names[i]+str(int(self.list_values1[i]))+_(' Level: ')+str(int(self.list_values2[i]))):
                self.update_flag = False
        
        if self.update_flag or threades.facilities_update_flag or threades.total_update_flag:
            
            self.list_values1 = (model.House.get_original_number(),model.School.get_original_number(),model.Hospital.get_original_number(),model.Workshop.get_original_number(),model.Farm.get_original_number(),model.Fountain.get_original_number())
            self.list_values2 = (model.House.get_level(),model.School.get_level(),model.Hospital.get_level(),model.Workshop.get_level(),model.Farm.get_level(),model.Fountain.get_level())
            pygame.draw.rect(threades.screen,(0,0,0),threades.resize_rect((930,40,270,350))) 
            for i in range(6):
    
                if not (self.value_labels[i].text == self.list_names[i]+str(int(self.list_values1[i]))+_(' Level: ')+str(int(self.list_values2[i]))):
                    self.value_labels[i].text = self.list_names[i]+str(int(self.list_values1[i]))+_(' Level: ')+str(int(self.list_values2[i]))
        
        self.update_flag = False
        


class mini_map:

    def __init__(self):
        
        self.update_flag = True
        for i in range(6):
            load_images.Map_images[i] = pygame.transform.scale(load_images.Map_images[i],threades.resize_pos((15,15)))
        self.map = pygame.image.load(os.path.join('data', 'map.png')).convert()
        self.map = pygame.transform.scale(self.map,threades.resize_pos((270,210)))
        self.list_num_fac = []
        for i in range(len(model.facilities_list)):
            self.list_num_fac.append(model.facilities_list[i].get_original_number())
    
    def update(self):
        
        for i in range(len(model.facilities_list)):
            if not (self.list_num_fac[i] == model.facilities_list[i].get_original_number()):
                self.update_flag = True
    
        if self.update_flag or threades.map_update_flag or threades.total_update_flag:
            threades.screen.blit(self.map,threades.resize_pos((930,390)))
            posn = threades.resize_pos((930+int(3200/33.3),390+int(2600/28.57)))
            threades.screen.blit(load_images.Map_images[6],posn)
            for i in range(len(model.facilities_list)):
                for j in range(model.facilities_list[i].get_original_number()):
                    posn = threades.resize_pos((930+int(load_images.facilities_posn_list[i][j][0]/33.3),390+int(load_images.facilities_posn_list[i][j][1]/28.57)))
                    threades.screen.blit(load_images.Map_images[i],posn)
        
        self.update_flag = False
    



class display_panel:

    def __init__(self):
        self.ind = indicator_panel()
        self.res = resources_panel()
        self.man = manpower_panel()
        self.fac = facilities_panel()
        self.map = mini_map()


    def update(self):
        self.ind.update_value()
        self.res.update_value()
        self.map.update()
        self.man.update_value()
        self.fac.update_value()
