# Adding variety to the responses.

# importing random module
import random

# Creating Templates
bot_template = "Bot: {0}"
user_template = "User: {0}"

# Variables
name = "Manu"
weather = "cloudy"

# Define a dictionary containing a list of responses for each message
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"],
  "bye": ["bye bye!", "bye! see you soon :)", "Bye, Take care!"]
}

# Use random.choice() to choose a matching response
def respond(message):
    if message in responses:
        bot_message = random.choice(responses[message])
    else:
        bot_message = random.choice(responses["default"])
    return bot_message

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

print("Hi! I am a chatbot. \nAsk me anything ;) ")
print("To end the conversation, tell me 'bye' :) ")
while True:
	question = input()
	send_message(question)
	if question == "bye":
		exit(0)