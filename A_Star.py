# Yeah this just does A* I guess
import math


def_board = [[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]


neighbor_rel = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def run():
    print_board(def_board)
    while True:
        #start_pos = list(map(int, input('Starting position: ').split(' ')))  # Formats to: [x, y]
        #end_pos = list(map(int, input('Ending position: ').split(' ')))
        start_pos = [0, 0]
        end_pos = [9, 9]

        a_star(def_board, start_pos, end_pos)
        break




def a_star(board, start, end):
    open_list = [start]
    closed_list = []

    # f-score = g-score + h-score
    g_score = [0]
    start_h = math.sqrt((abs(start[0]-end[0])**2)+math.sqrt(abs(start[1]-end[1])**2))
    f_score = [start_h]
    h_score = [start_h]

    while open_list:
        n = min(open_list)
        if n == end:
            break

        open_list.remove(n)

        neighbor_list = []
        for rel_pos in neighbor_rel:
            neighbor_pos = []
            for coord in range(2):
                neighbor_coord = n[coord] + rel_pos[coord]
                if neighbor_coord not in range(10):
                    break
                else:
                    neighbor_pos.append(neighbor_coord)
            if len(neighbor_pos) == 2:
                neighbor_list.append(neighbor_pos)

        print(neighbor_list)
        break












def print_board(board):     # Honestly just makes it easier to the eyes
    for row in board:
        for col in row:
            print(col, end=' ')
        print('')











if __name__ == "__main__":
    run()