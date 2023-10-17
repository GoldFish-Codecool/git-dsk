import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the initial number of guesses
max_guesses = 5

print("Welcome to the Random Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100. You have {max_guesses} guesses to find it.")

for guess_count in range(1, max_guesses+1):
    try:
        guess = int(input(f"Guess #{guess_count}: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the secret number ({secret_number}) in {guess_count} guesses!")
        break
else:
    print(f"Sorry, you've run out of guesses. The secret number was {secret_number}. Better luck next time!")
