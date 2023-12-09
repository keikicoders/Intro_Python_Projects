from random import randint

welcome_message = """
    Welcome to [Fill in your name here] 'Guess The Number'!

    In this app, you'll need to guess a number between
    [** the range specified **]. You have [**enter number of turns**] turns to guess correctly. 
    If you guess within [**enter number of turns**] turns, you'll be told how many
    turns it took you to guess. If you can't guess, a 
    losing message will be displayed along with the 
    random number.
"""
# Hint: the 'num_guesses_allowed' cannot be 0
num_guesses_allowed = ?
num_guesses = 0
# Hint: the 'random_number' must be a range
random_number = randint(?, ?)
user_won = False

print(welcome_message)

for turn in range(num_guesses_allowed):
    user_guess = int(input("What is your guess? "))
    num_guesses += 1

    # Fill in the missing code below in the "??"
    # Hint: Use if / else 
    
    # Where should you put the if statement?
    ?? user_guess == random_number:
        print("That's correct!")
        print(f"You guessed the number in {num_guesses} guesses.")
        user_won = True
    # Where should you put the else statement?
    ??:
        print("Sorry, that's incorrect, try again!")


if not user_won:
    print(f"Game over! The random number was: {random_number}.")
