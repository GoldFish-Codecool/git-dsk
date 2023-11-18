from area import *

Area1 = Area(1)
Area1.intro = "Welcome to the Hyatt Hotel. Now you should choose a way how to reach the stadium?"
Area1.choices = ["By walk", "By the standard bus", "By the bulletproof bus", "By the empty s-class Mercedes"]
Area1.outros = []
Area1.attribute_updates = []
Area1.next_area = [2,3,4,5] 

#do this for all 21 areas

area_list = [Area1, Area2, Area3] # up to the total numbers that we have; use this to navigate
# to switch between areas: this can be imported into the main.py and use area_list as a normal variable with list indexing