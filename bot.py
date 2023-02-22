# Import Python Coding Libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Instantiate the BOT
chatbot = ChatBot("Chatpot") 

# TRAINER 
"""If you pass an iterable with exactly two items to ListTrainer.train(), 
then ChatterBot considers the first item a statement and the second item an acceptable response.
If you provide longer lists of training conversations, 
then this will establish each item in the list as a possible response to its predecessor in the list."""

# Instantiate the trainer
trainer = ListTrainer(chatbot)

# Inserts entries into the database to build upon the graph structure the BOT uses to choose possible replies
# 1st training round
trainer.train([
    "Hi.",
    "Hello, I am Doug. How may I help you?"
])
# 2nd training round
trainer.train([
    "Are you a robot?",
    "Yes, I am an AI language model."
])
trainer.train([
    "How do you enter a sales order?",
    "Log in to the STORIS system using your user credentials. Click on the Sales module from the main menu.Click on Sales Order Entry to create a new sales order.Enter the customer information, including their name, address, phone number, and email address."
])

#EXIT CONDITIONS
exit_conditions = (":q", "quit", "exit") # Tuple of exit conditions to end while loop
while True: 
    query = input("> ") # Get input from user and save it to query
    if query in exit_conditions: # If user input in exit conditions break while loop
        break
    else:
        print(f"🤖 {chatbot.get_response(query)}") # Takes user input and gets a response
