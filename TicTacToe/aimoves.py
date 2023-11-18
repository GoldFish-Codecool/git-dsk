import random

def get_computer_moves(table):
available_moves = []

  
for i in [1,3,5]:
    
           
            row, col = 2 * (ord(move[0]) - ord('A')) + 1, 2 * (int(move[1]) - 1) + 1
           
           
            if table[row][col] != '.':
                print("That space is already taken. Try again.")
                continue
            break
    
    

my_list = [1, 2, 3, 4, 5]
rand_element = random.choice(my_list)
print(rand_element)
    
    
    return row, col