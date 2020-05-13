

# A "simple?" A* program in python
# ==============================================================================================================
# Future Changes Notes:
# so far, exceptions have yet to be added (for BadValues, for EmptyValues, for OutOfBoundsValues)
# more comments are also going to be added soon
# I also will be implementing this to pygame for a visual interface soon, along with the a process view
# I'll also make a version of this that takes advantage of classes instead of just using dictionaries


import math, pprint

# A Simple 9x9 Board
def_board = [[0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0]]

# A Simple 9x9 Maze Board
maze_board = [[0, 1, 0, 0, 1, 0, 0, 0, 1],
              [0, 1, 0, 1, 1, 0, 1, 0, 1],
              [0, 0, 0, 0, 0, 0, 1, 1, 0],
              [0, 1, 0, 1, 1, 0, 0, 1, 0],
              [1, 1, 0, 0, 0, 1, 1, 1, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0],
              [1, 1, 0, 1, 0, 1, 0, 1, 0],
              [1, 0, 0, 1, 0, 1, 0, 0, 1],
              [1, 0, 1, 0, 0, 0, 1, 0, 0]]

# Relative Positions of each neighbor
neighbor_rel = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def run():
    # start_pos = tuple(map(int, input('Starting position("x y"): ').split(' ')[::-1]))  # Formats to: [x, y]
    # end_pos = tuple(map(int, input('Ending position("x y"): ').split(' ')[::-1]))
    start_pos = (0, 0)
    end_pos = (8, 8)

    result = a_star(def_board, start_pos, end_pos)
    if not result:
        print('There is no path possible in this board')
    else:
        print('The shortest path from start to end is:\n' + str(result))
        print('Board:')
        for pos in result:
            def_board[pos[0]][pos[1]] = 2
        print_board(def_board)


def a_star(board, start, end):
    open_list = [start]
    closed_list = []
    parent_list = {start: None}

    # f(start_h) = h(start_h) + g(0)
    g_score = {start: 0}
    start_h = distance(start, end)
    f_score = {start: start_h}


    while len(open_list) > 0:
        # Get the key with the minimum f-score
        n = min(f_score, key = f_score.get)


        if n == end:
            path = [n]
            while True:
                n = parent_list[n]
                if n == None:
                    break
                path.insert(0, n)
            return path

        # Finds all neighbors in list, Makes a generator object (No noticable performance gain)
        neighbors = [tuple([sum(x) for x in zip(n, rel_pos)]) for rel_pos in neighbor_rel]

        for neighbor in neighbors:
            move_dist = distance(neighbor, n)
            newG_score = g_score[n] + move_dist
            if not(neighbor[0] in range(len(board[0])) and neighbor[1] in range(len(board))):
                continue
            elif board[neighbor[0]][neighbor[1]] == 1:
                continue
            elif neighbor in closed_list:
                continue

            if move_dist > 1:
                pos_checks = list(zip(n, neighbor[::-1]))
                if board[pos_checks[0][0]][pos_checks[0][1]] == 1 and board[pos_checks[1][1]][pos_checks[1][0]] == 1:
                    continue

                # (4, 4) -> (5, 5)
                # (4, 5), (5, 4)
            if newG_score < g_score.get(neighbor, newG_score + 1):
                parent_list[neighbor] = n
                g_score[neighbor] = newG_score
                f_score[neighbor] = newG_score + distance(n, end)
                if neighbor not in open_list:
                    open_list.append(neighbor)

        open_list.remove(n)
        closed_list.append(n)
        f_score.pop(n)
        g_score.pop(n)


    return False


# Just to make the numbers easier on the eyes
def print_board(board):
    for row in board:
        for col in row:
            print(col, end=' ')
        print('')


# The distance formula
def distance(pos_0, pos_1):
    return round(math.sqrt((pos_0[0] - pos_1[0]) ** 2  +  (pos_0[1] - pos_1[1]) ** 2), 2)


# Starts the program up
if __name__ == "__main__":
    run()