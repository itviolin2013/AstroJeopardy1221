# things that i am writing are here and popping up hopefully
# We will use this to suppress some warnings that are not important
import warnings
import litellm
import os
import numpy as np
import csv
import time


# Suppress specific Pydantic warnings that clutter the output
warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

# We will use dotenv to read the .env file
from pathlib import Path
from dotenv import load_dotenv


# Find .env in this directory or a parent (so it works when run via %run from another notebook)
_dir = Path(os.getcwd())
for _ in range(10):
    _env = _dir / ".env"
    if _env.exists():
        load_dotenv(_env)
        break
    _dir = _dir.parent
else:
    load_dotenv()

# This import will return an error if LiteLLM is not installed 


# Use this to measure response time

# URL of Ohio State's LiteLLM proxy server
custom_api_base = "https://litellmproxy.osu-ai.org" 

# Our API key for Astronomy 1221 (keep this private to our class)
astro1221_key = os.getenv("ASTRO1221_API_KEY")
if astro1221_key:
    print("Successfully loaded Astronomy 1221 key")
else:
    print("Error: did not find key. Check that .env exists in the same folder/directory as your class notebooks")

# Check that .gitignore exists in this directory
if os.path.isfile('.gitignore'):
    print("Successfully found .gitignore in the current directory")
else:
    print("Error: Did not find .gitignore. Please download .gitignore from carmen and put in the same folder/directory as your class notebooks.")

with open('.gitignore', 'r') as f:
    content = f.read()
    
    if '.env' in content:
        print("Confirmed that .gitignore has the .env exclusion")
    else: 
        print("Error: Did not find .env in .gitignore. Please download .gitignore from carmen and put with your class notebooks.")



def prompt_llm(messages, model="openai/GPT-4.1-mini", temperature=0.2, max_tokens=1000):
    """
    Send a prompt or conversation to an LLM using LiteLLM and return the response.

    Parameters:
        messages: Either a string (single user prompt) or a list of message dicts with
                  "role" and "content". If a string, formatted as [{"role": "user", "content": messages}].
        model (str, optional): The name of the model to use. Defaults to "openai/GPT-4.1-mini".
        temperature (float, optional): Value between 0 and 2; higher values make output more random. Defaults to 0.2.
        max_tokens (int, optional): Maximum number of tokens to generate in the completion. Must be a positive integer. Defaults to 1000.

    Prints the answer returned by the model.
    
    Returns:
        response: The full response object from LiteLLM.

    Raises:
        ValueError: If `temperature` is not in [0, 2] or `max_tokens` is not a positive integer.
    """
    # If messages is a string, format it as a single user message
    if isinstance(messages, str):
        messages = [{"role": "user", "content": messages}]
    # Validate temperature
    if not (isinstance(temperature, (int, float)) and 0 <= temperature <= 2):
        raise ValueError("temperature must be a float between 0 and 2 (inclusive).")
    # Validate max_tokens
    if not (isinstance(max_tokens, int) and max_tokens > 0):
        raise ValueError("max_tokens must be a positive integer.")

    try: 
        #print("Contacting LLM via University Server...")

        response = litellm.completion(
            model=model,
            messages=messages,
            api_base=custom_api_base,
            api_key=astro1221_key,
            temperature=temperature,
            max_tokens=max_tokens
        )

        answer = response['choices'][0]['message']['content']
        #print(f"\nSUCCESS! Here is the answer from {model}:\n")
        #print(answer)
        #print("\n")

    except Exception as e:
        print(f"\nERROR: Could not connect. Details:\n{e}")    
        answer = None

    return answer

def show_response_metadata(response):
    '''
    Convert the response to a dictionary
    Print information about token usage and costs
    '''
    
    # Here are the top level keys
    response_dict = response.model_dump()
    # print(f"Top-level keys: {response_dict.keys()}\n")
    
    # Here are more details: 
    # 1. Get the exact model version used by the server
    used_model = response.model
    
    # 2. Extract token counts from the 'usage' attribute
    input_tokens = response.usage.prompt_tokens
    output_tokens = response.usage.completion_tokens
    total_tokens = response.usage.total_tokens
    
    # 3. Calculate the cost (LiteLLM does the math based on current rates)
    cost = litellm.completion_cost(completion_response=response)
    
    print(f"--- Query Metadata ---")
    print(f"Model:        {used_model}")
    print(f"Input Tokens: {input_tokens}")
    print(f"Output Tokens:{output_tokens}")
    print(f"Total Tokens: {total_tokens}")
    print(f"Estimated Cost: ${cost:.6f}") # Showing 6 decimal places for small queries
    


# check path location to make sure directory is correct
current_dir = os.getcwd()

# make sure the file is in our directory
if os.path.exists("astro_jeopardy_answers.csv"):
    print("astro_jeopardy_answers.csv exists in the current directory.")
else:
    print("astro_jeopardy_answers.csv does not exist in the current directory.")

# read the file
def create_answers():
    with open("astro_jeopardy_answers.csv", "r") as file:
        reader = csv.reader(file)
        try:
            answer = np.genfromtxt("astro_jeopardy_answers.csv", delimiter=",", dtype=str)
            # print("Data array created successfully.")
            # print(f"The array's shape is {answer.shape}.")
            answer = answer.flatten()
            # print(answer)
        except Exception as e:
            print(f"Error creating data array: {e}")
    return answer




# check path location to make sure directory is correct
current_dir = os.getcwd()

# make sure the file is in our directory
if os.path.exists("astro_jeopardy_facts.csv"):
    print("astro_jeopardy_facts.csv exists in the current directory.")
else:
    print("astro_jeopardy_facts.csv does not exist in the current directory.")

# read the file
# Note: np.genfromtxt expects the SAME number of columns on every row.
# The header has no @ (1 column), but fact lines have @ at start (2 columns) -> "got 2 columns instead of 1"
# Fix: read line-by-line and extract the fact text (everything after @)
# Also deletes the @ when it reads the file so it doesnt show up in the facts or anything
#The array is flattened so that it is not in 2D 


with open("astro_jeopardy_facts.csv", "r") as file:
    reader = csv.reader(file)
    try:
      facts = np.genfromtxt("astro_jeopardy_facts.csv", delimiter="@", dtype=str)
      facts = facts.flatten()
    except Exception as e:
       print(f"Error creating data array: {e}")

"""
    next(file)  # skip header row
    for line in file:
        line = line.strip()
        if line.startswith("@"):
            facts_list.append(line[1:].strip())  # remove @ and get fact text
        # skip merge conflict lines and other non-fact lines
    #facts = np.array(facts_list)
    desired_shape = (5, 6)
    #facts2 = np.array(facts_list).reshape(desired_shape)
    print("Data array created successfully.")
    #print(f"The array's shape is {facts2.shape}.")
    #print(facts2)  # Show first 3 facts
    print(facts_list)
    """

answer = create_answers()

#zip make it run through both lists at the same time
#the chat assignment tells the llm almost who it is and tells it the answer is the i or facts_list and the j ot answer
#the clues is an empty list that eventually gets filled with the clue function
# The reshape function is used to make the array 5 rows and 6 columns instead of having it as one long array
#the chat assignment tells the AI to act as if it is Alex Trebek hosting a game of Astronomy-themed Jeopardy so that questions are generated in a way that makes it feel llike you are participating in the actual game


def create_clues(answer):
    clues = []

    for i, j in zip(facts, answer):
        chat_assignment = f"""You are Alex Trebek hosting a game of Astronomy-themed Jeopardy. Generate one Jeopardy-style
            clue using the given facts, with the answer being {j}.
            Do not mention the answer in the prompt, and only include the clue in your response."""
        messages = [{"role": "system", "content": chat_assignment}, 
            {"role": "user", "content": i}]
        clue = prompt_llm(messages)
        clues.append(clue)
    cluesArray = np.array(clues)
    cluesArray = cluesArray.reshape(5, 6)
    answerArray = answer.reshape(5, 6)
    print(f"Clues generated successfully.")
    return cluesArray, answerArray

def compare_answer(correctAnswer, answerInput):
    chat_assignment = f"""This is a game of Jeopardy and you will be given the player's guess to the answer. 
                        The correct answer to the question is "What is {correctAnswer}?" (or "Who is {correctAnswer}?" if the 
                        correct answer is a person). Grade the player's guess and 
                        respond ONLY with "Correct", "Incorrect", or "Please respond with your answer formatted as a question." 
                        according in accordance with the parameters provided: If the player makes a minor spelling error (ex. 
                        guessing "What is the molky way?" instead of "what is the milky way?"), the answer should still be 
                        marked as correct. If the player gives a common synonym or alternate name for the answer, (ex. guessing 
                        "What is the Andromeda Galaxy?" instead of "What is M31?"), the answer should still be marked as correct. 
                        The player must respond with the answer formatted as a question, otherwise you should respond with "Please 
                        respond with your answer formatted as a question." Any other guess that does not fall into these parameters
                        should be marked as incorrect."""
    messages = [{"role":"system", "content": chat_assignment}, 
                {"role": "user", "content": answerInput}]
    chatAnswer = prompt_llm(messages)
    print(chatAnswer)
    return chatAnswer

compare_answer("M31", "What is the Andromeda Galaxy?")
# The compare_answer function is used to compare the player's guess to the correct answer
# There are some parameters that are used to make sure that the player's guess is formatted correctly as a question like if they were actively playing
#The response is said to either be correct, incorrect, or have it said it needs to be formatted as a question. Later in the code there is something that allows a player to try the question again if the formstting is not correct 


