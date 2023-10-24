#Excercise 3 Find the largest number
import sys
largest_number = 0
all_numbers = []


count = int (input ("How many numbers do you want to compare? "))
if count <= 0:
  print ("The number has to be bigger than Zero")
  sys.exit()

for i in range(count):
  number = int (input (f'Enter number {i+1}: \n'))
  all_numbers.append (number)
  if i == 0 :
    largest_number = number
  if number > largest_number :
    largest_number = number

print (f"Your number set consists of {all_numbers} and the largest number is {largest_number} \n")
