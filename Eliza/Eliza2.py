# Extracting key phrases

# The really clever thing about ELIZA is 
# the way the program appears to understand what you told it by occasionally including phrases uttered by the user in its responses.

# We will match messages against some common patterns and extract phrases using re.search(). 
# A dictionary called rules has been defined, which matches the patterns.
import re
import random

rules = {'I want (.*)': ['What would it mean if you got {0}',
  	'Why do you want {0}',
  	"What's stopping you from getting {0}"],
 	'do you remember (.*)': ['Did you think I would forget {0}',
  	"Why haven't you been able to forget {0}",
  	'What about {0}',
  	'Yes .. and?'],
 	'do you think (.*)': ['if {0}? Absolutely.', 'No chance'],
 	'if (.*)': ["Do you really think it's likely that {0}",
  	'Do you wish that {0}',
  	'What do you think about {0}',
  	'Really--if {0}']}


# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None
    
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response.format(phrase)

print(replace_pronouns("my last birthday"))
print(replace_pronouns("when you went to Florida"))
print(replace_pronouns("I had my own castle"))