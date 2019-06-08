# Asking questions is a great way to create an engaging conversation. 
# Here, we'll create the very first hint of ELIZA's famous personality, 
# by responding to statements with a question and responding to questions with answers.


import random

# Creating Templates
bot_template = "Bot: {0}"
user_template = "User: {0}"

# # Variables
# name = "Manu"
# weather = "cloudy"

# A dictionary of responses
responses = {'question': ["I don't know :(", 'you tell me!'],
 			'statement': ['tell me more!',
  			'why do you think that?',
  			'how long have you felt this way?',
  			'I find that extremely interesting',
  			'can you back that up?',
  			'oh wow!',
  			':)']}


def respond(message):
    # Check for a question mark
    if message.endswith('?'):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")
