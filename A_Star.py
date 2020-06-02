import math

def_board = [[0, 0, 0, 0, 1, 0, 0, 0, 0],    # While stuff is still being tested
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0]]

class Board:
    """
        A Board Class contains a 2D Array of Node objects
    """
    def __init__(self, config, start):
        self.board = [[Node(col, row, distance((col, row), (start[0], start[1])))
                      for col in config[0]]
                      for row in config]
        


    def __str__(self):
        return_str = ''
        for row in def_board:
            for col in row:
                return_str += str(col) + ' '
            return_str += '\n'

        return return_str
    
    def distance(self, pos_0, pos_1):
        return round(math.sqrt((pos_0[0] - pos_1[0]) ** 2  +  (pos_0[1] - pos_1[1]) ** 2), 2)

class Node:
    """
    A Node Class is any value in the board that is used in the program
    """
    def __init__(self, x, y, value, h, g = None, parent = None):
        self.x = x
        self.y = y
        
        self.g = g
        self.h = h

        self.f = self.g + self.h


def run():
    board = Board(def_board)
    print(board)

if __name__ == "__main__":
    run()