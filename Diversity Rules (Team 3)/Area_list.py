from area import *

Area1 = Area(1)
Area1.intro = "Welcome to the Hyatt Hotel. Now you should choose a way how to reach the stadium?"
Area1.choices = ["By walk", "By the standard bus", "By the bulletproof bus", "By the empty s-class Mercedes"]
Area1.outros = ["Outro 1", "Outro 2", "Outro 3", "Outro 4"]
Area1.attribute_updates = [{"health": -1, "alcohol": 1, "chairman": 0}, {"health": -1, "alcohol": 0, "chairman": -1}, {"health": -1, "alcohol": 0, "chairman": -1}, {"health": -1, "alcohol": 0, "chairman": -1}]
Area1.next_area = [2,3,4,5]

Area2 = Area(2)
Area2.intro = "Welcome to the Hyatt Hotel. Now you should choose a way how to reach the stadium? 222"
Area2.choices = ["By walk 2", "By the standard bus 2", "By the bulletproof bus 2", "By the empty s-class Mercedes 2"]
Area2.outros = []
Area2.attribute_updates = []
Area2.next_area = [6,7,8,9]

#do this for all 21 areas

area_list = [Area1, Area2, Area3] # up to the total numbers that we have; use this to navigate
# to switch between areas: this can be imported into the main.py and use area_list as a normal variable with list indexing