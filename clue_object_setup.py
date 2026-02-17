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
        

board = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]])


i = 0
for row in board:
    for element in row: 
        i += 1  # or i += 0 if you really just want a no-op; i must be defined first
        

tile1 = Tile("hello", "goodbye", True, 100, False)
print(tile1)

board = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24], [25, 26, 27, 28, 29, 30]])

