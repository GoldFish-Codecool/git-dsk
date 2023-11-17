from area import area

Area1 = area(1)
Area1.intro = ""
Area1.choices = []
Area1.outros = []
Area1.attribute_updates = []
Area1.next_area = [] #reachable area ID

#do this for all 21 areas

area_list = [Area1, Area2, Area3] # up to the total numbers that we have; use this to navigate
# to switch between areas: this can be imported into the main.py and use area_list as a normal variable with list indexing