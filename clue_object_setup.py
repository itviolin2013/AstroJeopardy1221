# clue_object_setup.ipynb

import numpy as np
from AI_Setup import prompt_llm

class Tile:
    """Class for each tile"""

    def __init__(self, clue, answer, isDailyDouble, pointValue, beenUsed):
        self.clue = clue
        self.answer = answer
        self.isDailyDouble = isDailyDouble
        self.pointValue = pointValue
        self.beenUsed = beenUsed

    def __str__(self):
        return self.clue

    def __lt__(self, other):
        return self.pointValue < other.pointValue

class Player:
    """Class for the player"""
    def __init__(self, playerName, playerOccupation, playerAge, playerTown):
        self.playerName = playerName
        self.playerOccupation = playerOccupation
        self.playerAge = playerAge
        self.playerTown = playerTown

        #player information
#print("Hello, Welcome to AstroJeopardy! Please enter user information.")
#name = input("Enter your name: ")
#age = input("Enter your age: ")
#occupation = input("Enter your occupation: ")
#location = input("Enter your location: ")

#player1 = Player(name, occupation, age, location)

#print(f"Ready to play, {player1.playerName}?")

board = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]])

#Allowing Ai to converse to learn more about the player based on the information provided.

def get_player_info_via_ai():
    """Uses the LLM to conversationally collect player info based on what the user provides."""
    
    system_prompt = """You are a welcoming a charasmatic Jeopardy host welcoming a new player to AstroJeopardy. Your job is to collect more information based on the information provided:
    - name
    - age
    - occupation
    - location (town/city)
    
    Ask ONE question at a time. React naturally to what they say (e.g., if they mention they're a student, ask what they study). 
    When you have all four pieces of info, respond with ONLY this line:
    DONE|name|age|occupation|location
    (replace with the actual values). Keep your questions friendly and brief."""
    
    messages = [{"role": "system", "content": system_prompt}]
    
    while True:
        user_input = input("\nYou: ")
        messages.append({"role": "user", "content": user_input})
        
        response = prompt_llm(messages, temperature=0.3)
        if response is None:
            print("Error contacting LLM.")
            break
            
        ai_text = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": ai_text})
        
        # Check if AI signaled that we have all info
        if ai_text.strip().startswith("DONE|"):
            parts = ai_text.strip().split("|")[1:5]  # name, age, occupation, location
            return Player(parts[0], parts[1], parts[2], parts[3])

i = 0
for row in board:
    for element in row: 
        i += 1  # or i += 0 if you really just want a no-op; i must be defined first
        

tile1 = Tile("hello", "goodbye", True, 100, False)
print(tile1)

print("Hello, Welcome to AstroJeopardy! Please enter user information.")
name = input("Enter your name: ")
age = input("Enter your age: ")
occupation = input("Enter your occupation: ")
location = input("Enter your location: ")

player1 = Player(name, occupation, age, location)

print(f"Ready to play, {player1.playerName}?")

board = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]])

#Allowing Ai to converse to learn more about the player based on the information provided.


def get_player_info_via_ai():
    """Uses the LLM to conversationally collect player info based on what the user provides."""
    
    system_prompt = """You are a welcoming a charasmatic Jeopardy host welcoming a new player to AstroJeopardy. Your job is to collect more information based on the information provided:
    - name
    - age
    - occupation
    - location (town/city)
    
    Ask ONE question at a time. React naturally to what they say (e.g., if they mention they're a student, ask what they study). 
    When you have all four pieces of info, respond with ONLY this line:
    DONE|name|age|occupation|location
    (replace with the actual values). Keep your questions friendly and brief."""
    
    messages = [{"role": "system", "content": system_prompt}]
    
    while True:
        user_input = input("\nYou: ")
        messages.append({"role": "user", "content": user_input})
        
        response = prompt_llm(messages, temperature=0.3)
        if response is None:
            print("Error contacting LLM.")
            break
            
        ai_text = response['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": ai_text})
        
        # Check if AI signaled that we have all info
        if ai_text.strip().startswith("DONE|"):
            parts = ai_text.strip().split("|")[1:5]  # name, age, occupation, location
            return Player(parts[0], parts[1], parts[2], parts[3])