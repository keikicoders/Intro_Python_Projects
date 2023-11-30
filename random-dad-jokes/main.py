from random import choice


def get_random_joke():
    jokes = [
        {"setup": "Why don't eggs tell jokes?", "punchline": "They'd crack each other up."},
        {"setup": "I'm reading a book on anti-gravity.", "punchline": "It's impossible to put down!"},
        {"setup": "Did you hear about the mathematician who's afraid of negative numbers?", "punchline": "He'll stop at nothing to avoid them."},
        {"setup": "Why are bank tellers not allowed to ride bicycles?", "punchline": "They tend to lose their balance."},
        {"setup": "What do you call a fish wearing a crown?", "punchline": "A king fish."},
    ]
    return choice(jokes)


def display_joke(joke):
    punchline = joke["punchline"]
    setup = joke["setup"]
    print(f"Setup: {setup}")
    input("[Press `Enter` to hear the punchline...]")
    print(f"Punchline: {punchline}")


welcome_message = """
    Welcome to the `Random Dad Joke` app!

    This app uses an API to fetch a random setup
    and punchline to a dad joke. The setup will
    be displayed to you, and if you guess the punchline,
    a message like "That's correct!" will be displayed.
    Otherwise, you'll be shown the punchline.
"""

options = """
    (1) Get Dad Joke (2) Exit
"""

GET_JOKE = 1
EXIT = 2

while True:
    user_choice = int(input(options))

    if user_choice == GET_JOKE:
        random_joke = get_random_joke()
        display_joke(random_joke)
    elif user_choice == EXIT:
        break
