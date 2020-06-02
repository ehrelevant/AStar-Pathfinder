class board:
    def_board =[[0, 0, 0, 0, 1, 0, 0, 0, 0],    # While stuff is still being tested
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0]]

    def print_board(self):
        for row in def_board:
            for col in row:
                print(col, end=' ')
            print('')


class node:
    def __init__(self, g, h):
        self.g = g
        self.h = h

        self.f = self.g + self.h