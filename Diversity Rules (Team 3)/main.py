from area import *

from Area_list import *

from player import *

# player to know which is the location

# instantiate area list
# instantiate player
# make it work in "general" and then invoke all methods from the area list
def get_user_choice():
    choices = area_list[0].choices # we need to put player location for the others
    for choice in choices:
        print (choice)        
    
    while True:
        print("Select a choice:")
        #for key, value in choices.items():
            #print(f"{key}: {value}")

        user_input = input("Enter the number of your choice: ")

        if user_input in choices:
            return choices[user_input]
        else:
            print("Invalid choice. Please try again.")


get_user_choice()
