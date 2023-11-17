from area import area

from Area_list import *

from player import *

# instantiate area list
# instantiate player
# make it work in "general" and then invoke all methods from the area list
def get_user_choice():
    choices = {
        '1': 'Choice 1',
        '2': 'Choice 2',
        '3': 'Choice 3',
        '4': 'Choice 4',
    }
    while True:
        print("Select a choice:")
        for key, value in choices.items():
            print(f"{key}: {value}")

        user_input = input("Enter the number of your choice: ")

        if user_input in choices:
            return choices[user_input]
        else:
            print("Invalid choice. Please try again.")



