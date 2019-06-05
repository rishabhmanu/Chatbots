# A bot which can answer simple questions such as "What's your name?" and "What's today's weather?"
# We will use a dictionary with these questions as keys and the correct responses as values.
# This means the bot will only respond correctly if the message matches exactly, which is a big limitation.

# Creating Templates
bot_template = "Bot: {0}"
user_template = "User: {0}"

# Define variables
name = "Manu"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "bye": "Bye bye!",
  "default": "default message"
}

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message

print("Hi! I am a chatbot. \nAsk any question here ;) ")
while True:
	question = input()
	send_message(question)
	if question == "bye":
		exit(0)