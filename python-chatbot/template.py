from random import choice

welcome_message = """
    Welcome to [**Enter names here**] "Zodiac Chatbot" app!

    This is a chatbot that you can send commands
    to and it will perform some action. The five recognized
    commands are shown below:

        1. Tell me your name
            - Responds with: "[**Enter response here**]"

        2. [**Enter own command here**]
            - Responds with: [**Chatbot response here**]

        3. Random zodiac fact
            - Responds with a random fact, such as:
                - "Aries (March 21 - April 19) is the first sign of the zodiac, symbolized by the Ram, and is known for its energetic and pioneering nature.",

        4. Goodbye
            - Responds with "See ya later!" and exits the app

        5. BONUS: [**Enter your own command here**]
            - [**Enter the chatbot response here**]

    Any command sent outside of the ones listed above will result
    in the chatbot responding with: "Sorry, I don't know that command!"
"""

zodiac_facts = [
    "Aries (March 21 - April 19) is the first sign of the zodiac, symbolized by the Ram, and is known for its energetic and pioneering nature.",
    "Taurus (April 20 - May 20), symbolized by the Bull, is known for its reliability, practicality, and love of comfort and luxury.",
    "Gemini (May 21 - June 20), represented by the Twins, is known for its versatility, curiosity, and excellent communication skills.",
    "Cancer (June 21 - July 22), symbolized by the Crab, is known for its emotional depth, nurturing instincts, and strong ties to family and home.",
    "Leo (July 23 - August 22), symbolized by the Lion, is known for its confidence, creativity, and natural leadership qualities.",
    "Virgo (August 23 - September 22), represented by the Maiden, is known for its practicality, analytical skills, and attention to detail."
]

print(welcome_message)

while True:
    command = input("Enter your command: ")
    
    # Fill in the missing code below in the "??"
    # Hint: use if / elif / else
    ?? command.lower() ?? "tell me your name":
        print("Zodiac Facts Chatbot")
    ?? command.lower() ?? "[enter custom command here]":
        print("custom response here")
    ?? command.lower() ?? "random zodiac fact":
        random_fact = choice(zodiac_facts)
        print(random_fact)
    ?? command.lower() ?? "Goodbye":
        print("See ya later!")
        break
    ??:
        print("Sorry, I don't know that command!")
