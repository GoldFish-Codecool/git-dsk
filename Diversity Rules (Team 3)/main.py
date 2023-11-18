import sys
from area import *
from Area_list import *
from player import *

# player to know which is the location

# instantiate area list
# instantiate player
# make it work in "general" and then invoke all methods from the area list

print("\n\nWELCOME TO THE BEST GAME YOU EVER PLAYED!")
print("HAVE FUN!")
print("---")
print ("\n\nThe Wheel of fortune… You are thinking of the next OC and your and your direct reports’ OKRs completion status, while you do the last cross-check of your smart casual appearance in front of the mirror. After a long sight, you refocus your attention to less pressing matters: the football match tonight between Bulgaria and Hungary. Who will win tonight? Who should you be cheering for? Do you even care? How should you behave? Who will you be talking to? You leave to Hyatt to meet everyone at 18:45 sharp, knowing that from this point on you have full control over how the events of tonight unfold – but you will also need to own the consequences, let them be personal or professional...") 

player_name = input("\nEnter your name: ")

    
player1 = Player(player_name)

player_difficulty = int(input("\nEnter difficulty 1-easy 2-medium 3-hard :"))
if player_difficulty == 1:
    player1.update_chairman (5)
elif player_difficulty == 2:
    player1.update_chairman (2)
elif player_difficulty == 3:
    player1.update_chairman (0)
else:
    print ("Invalid choice")
    
print(f"\nWelcome {player_name} ")
print(f"\nYour health is {player1.health} ")
print(f"Your alcohol level is {player1.alcohol} ")
print(f"Your favor with the Chairman is {player1.chairman} ")
#player1.update_health(-1)
#player1.update_alcohol(1)
#player1.update_chairman(-1)
#print(f"Your health is {player1.health} ")
#print(f"Your alcohol level is {player1.alcohol} ")
#print(f"Your favor with the Chairman is {player1.chairman} ")

def get_user_choice():
          
    while True:
        choices = area_list[player1.location].choices # we need to put player location for the others
        next_area = area_list[player1.location].next_area
        intro = area_list[player1.location].intro
        outros = area_list[player1.location].outros
        attribute_updates = area_list[player1.location].attribute_updates
        
        print(intro)
        
        for i in range(len(choices)):
            print (i+1, choices [i]) 
        print("Select a choice:")
        
        user_input = int(input("Enter the number of your choice: "))-1

        if user_input in range(len(choices)):
            print(choices[user_input])
            print(outros[user_input])
            return user_input, next_area[user_input]-1
        elif user_input.lower() == "quit":
            print("You are exiting the game..Thank you for playing")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

new_area = 0

while True: # should be while not_game-over condition
    old_area = new_area
    user_input, new_area = get_user_choice()

    #print(player1.location, user_input, old_area)  
    health_update = area_list[player1.location].attribute_updates [user_input]["health"]
    player1.update_health(health_update)
    print(f"Your health is {player1.health} ")

    alcohol_update = area_list[player1.location].attribute_updates [user_input]["alcohol"]
    player1.update_alcohol(alcohol_update)
    print(f"Your alcohol level is {player1.alcohol} ")

    chairman_update = area_list[player1.location].attribute_updates [user_input]["chairman"]
    player1.update_chairman(chairman_update)
    print(f"Your chairman points are {player1.chairman} ")

    if player1.health < 1:
        print(f"Game over. Your health reached {player1.health}. Your are in hospital.")
        break
    elif player1.alcohol > 3:
        print(f"Game over. Your alcohol level exceeds {player1.alcohol} promils. Your are drunk and in jail.")
        break
    elif player1.chairman < -5:
        print(f"Game over. Your favour with the Chairman reached {player1.chairman}. Chairman had enough of you. You are fired.")
        break
    elif player1.location == 23:
        print("GAME OVER - YOU WERE TAKEN TO JAIL")
    elif player1.location == 22 and player1.chairman > 4:
        print(f"You are home safely. The next day you get a letter from the Chairman - you are promoted.")
        break
    elif player1.location == 22:
        print(f"You win. You are home safely.")
        break
    
    player1.location = new_area
       
    #user_input = input("Do you want to quit the game? (y/n): ")
    #if user_input == "y":
    #    sys.exit(0)
    
    #def exit_program():
    # sys.exit(0)
    
    #else:
    #player1.location = new_area
        