import random

number = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("I have selected a number between 1 and 100. Try to guess it: "))
    guesses += 1

    if guess < number:
        print("This is too low! Try again!")
    elif guess > number:
        print("Way too high! Try again!")
    else:
        print("Bang! You got it!")
        break

print("It took you", guesses, "guesses.")
