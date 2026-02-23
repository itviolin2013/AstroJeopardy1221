import numpy as np
from AI_Setup import prompt_llm
#creates a new class that allows the player to enter their name, age, occupation and location
#creates a new function that prompts the host to ask the player two to three questions (one at a time) based on their name, age, occupation and location 
#creates a new function that allows the player to answer the questions and the host to respond with the next question
#once the host has asked the player two to three questions and the player has answered them the host will respond with "Let's start playing!"


class Player:
    """Class for the player"""
    def __init__(self, playerName, playerOccupation, playerAge, playerTown, points=0):
        self.playerName = playerName
        self.playerOccupation = playerOccupation
        self.playerAge = playerAge
        self.playerTown = playerTown
        self.points = points

def host_chat_with_player(player):
    """LLM host asks 2-3 follow-up questions about the player, then asks if they're ready to play."""
    system_prompt = f"""You are a welcoming, charismatic Jeopardy host for AstroJeopardy. You have this player's info:
    - Name: {player.playerName}
    - Age: {player.playerAge}
    - Occupation: {player.playerOccupation}
    - Location: {player.playerTown}

    Your job: Ask exactly 2 or 3 short, friendly follow-up questions about them (e.g. what they study, what they're excited about). Ask ONE question per message. After they answer each, ask the next. After 2 or 3 questions total, respond with "Let's start playing!". Keep every message brief—one question or one "Let's start playing!" line only. Do not list multiple questions at once."""

    messages = [{"role": "system", "content": system_prompt}]
    max_rounds = 4  # 2-3 Q&A + "ready to play?"

    for _ in range(max_rounds):
        ai_text = prompt_llm(messages, temperature=0.3)
        if ai_text is None:
            print("Error contacting LLM.")
            return
        messages.append({"role": "assistant", "content": ai_text})
        print(f"\nHost: {ai_text.strip()}")
        if _ <= max_rounds:
            user_input = input("\nYou: ")
            messages.append({"role": "user", "content": user_input})

    return 

def startGame():
    print("Hello, Welcome to AstroJeopardy! Please enter user information.")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    occupation = input("Enter your occupation: ")
    location = input("Enter your location: ")
    player1 = Player(name, occupation, age, location)
    host_chat_with_player(player1)
    
    return player1



