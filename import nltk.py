import nltk
import random
from nltk.chat.util import Chat, reflections

# Define some conversation patterns
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you ?', ["I'm doing well, thank you!", "I'm great, thanks for asking."]),
    (r'what is your name ?', ["You can call me ChatBot.", "I'm ChatBot."]),
    (r'quit|exit', ["Goodbye!", "Bye, take care!"]),
    # Add more patterns and responses here
]

# Create a ChatBot with the defined patterns
chatbot = Chat(patterns, reflections)

# Start chatting
print("Welcome to ChatBot!")
print("Type 'quit' or 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
    if user_input.lower() in ['quit', 'exit']:
        break