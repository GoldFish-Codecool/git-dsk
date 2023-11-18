from area import *

from Area_list import *

from player import *

# player to know which is the location

# instantiate area list
# instantiate player
# make it work in "general" and then invoke all methods from the area list

player_name = input("Etner your name: ")
player1 = Player(player_name)
print(f"Welcome {player_name} ")
print(f"Your health is {player1.health} ")
print(f"Your alcohol level is {player1.alcohol} ")
print(f"Your favor with the Chairman is {player1.chairman} ")
player1.update_health(-1)
player1.update_alcohol(1)
player1.update_chairman(-1)
print(f"Your health is {player1.health} ")
print(f"Your alcohol level is {player1.alcohol} ")
print(f"Your favor with the Chairman is {player1.chairman} ")

def get_user_choice():
          
    while True:
        choices = area_list[player1.location].choices # we need to put player location for the others
        next_area = area_list[player1.location].next_area
        for i in range(len(choices)):
            print (i+1, choices [i]) 
        print("Select a choice:")
        
        user_input = int(input("Enter the number of your choice: "))-1

        if user_input in range(len(choices)):
            print(choices[user_input])
            return next_area[user_input]-1
        else:
            print("Invalid choice. Please try again.")

while True: # should be while not_game-over condition
    new_area = get_user_choice()
    player1.location = new_area

