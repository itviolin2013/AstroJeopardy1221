# clue_object_setup.py

import numpy as np

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
    board = np.array([[1, 2, 3, 4, 5, 6], 
                      [7, 8, 9, 10, 11, 12], 
                      [13, 14, 15, 16, 17, 18], 
                      [19, 20, 21, 22, 23, 24], 
                      [25, 26, 27, 28, 29, 30]])
    for row in range(5):
        for column in range(6):
            board[row][column] = Tile(clues[row][column], answers[row][column], pointValue[row][column], isDD[row][column], beenUsed[row][column])
    print(board[0, 0].answer)
    print(board)
    return board

