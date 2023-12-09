from random import choice

welcome_message = """
    Welcome to [Fill out your name here] `Random Dad Joke` app!

    This app uses a dictionary to fetch random dad jokes and
    setup punchlines. The setup will
    be displayed to you, and if you guess the punchline,
    a message like "That's correct!" will be displayed.
    Otherwise, you'll be shown the punchline.
"""

def get_random_joke():
    jokes = [
        {"setup": "Why don't eggs tell jokes?", 
         "punchline": "They'd crack each other up."},
        {"setup": "I'm reading a book on anti-gravity.", 
         "punchline": "It's impossible to put down!"},
        {}
        {}
        {},
    ]
    return choice(jokes)


def display_joke(joke):
    punchline = joke["punchline"]
    setup = joke["setup"]
    print(f"Setup: {setup}")
    input("[Press `Enter` to hear the punchline...]")
    print(f"Punchline: {punchline}")

options = """
    (1) Get Dad Joke (2) Exit
"""

GET_JOKE = 1
EXIT = 2

while True:
    user_choice = int(input(options))

    # Fill in the missing code below in the "??"

    # Hint What is the syntax for an if statement?
    ?? user_choice ?? GET_JOKE:
        # How do you assign a variable?
        random_joke ?? get_random_joke()
        display_joke(random_joke)
    # How do you check if a variable is equal to a value?
    ?? user_choice ?? EXIT:
        break
    # BONUS: add error handling here
