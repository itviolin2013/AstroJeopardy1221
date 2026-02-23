# clue_object_setup.py

import numpy as np
# Creates a bunch of empty variables to put into the board
t1 = None
t2 = None
t3 = None
t4 = None
t5 = None
t6 = None
t7 = None
t8 = None
t9 = None
t10 = None
t11 = None
t12 = None
t13 = None
t14 = None
t15 = None
t16 = None
t17 = None
t18 = None
t19 = None
t20 = None
t21 = None
t22 = None
t23 = None
t24 = None
t25 = None
t26 = None
t27 = None
t28 = None
t29 = None
t30 = None

# Creates a class to bundle variables together
# Within the class are methods that are able to be used, and allows for information to be identified manually

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
        
        
def generate_tiles(clues, answers, pointValue, isDD, beenUsed):
    board = np.array([[t1, t2, t3, t4, t5, t6], 
                      [t7, t8, t9, t10, t11, t12], 
                      [t13, t14, t15, t16, t17, t18], 
                      [t19, t20, t21, t22, t23, t24], 
                      [t25, t26, t27, t28, t29, t30]])
    for row in range(5):
        for column in range(6):
            board[row][column] = Tile(clues[row][column], answers[row][column], pointValue[row][column], isDD[row][column], beenUsed[row][column])
    print(board[0][0].answer)
    return board
# Function that actually generates the board
# The rows and colums each have a diffrent clue and answer based on catagories and point value
# The daily double function is used and called on a randon row and column in each game 

