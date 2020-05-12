

# A "simple?" A* program in python
# ==============================================================================================================
# Current Version Notes:
# so far, exceptions have yet to be added (for BadValues, for EmptyValues, for OutOfBoundsValues)
# diagonal movement and more comments are also going to be added soon
# I also will be implementing this to pygame for a visual interface soon, along with the a process view
# I'll also make a version of this that takes advantage of classes instead of just using dictionaries


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

neighbor_rel = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def run():
    start_pos = tuple(map(int, input('Starting position: ').split(' ')))  # Formats to: [x, y]
    end_pos = tuple(map(int, input('Ending position: ').split(' ')))
    path = a_star(def_board, start_pos, end_pos)

    print('The shortest path from start to end is:\n' + str(path))
    print('Board:')
    for pos in path:
        def_board[pos[0]][pos[1]] = 2
    print_board(def_board)


def a_star(board, start, end):
    open_list = [start]
    closed_list = []
    parent_list = {start: None}

    # Used something kinda like 2D Vector distance calculation
    # f(start_h) = h(start_h) + g(0)
    g_score = {start: 0}
    start_h = math.sqrt(abs(start[0] - end[0]) ** 2)  +  math.sqrt(abs(start[1] - end[1]) ** 2)
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

        # Finds all neighbors in list
        neighbor_list = []
        for rel_pos in neighbor_rel:
            neighbor_list.append(tuple([sum(x) for x in zip(*[n, rel_pos])]))

        for neighbor in neighbor_list:
            newG_score = g_score[n] + 1
            if not(neighbor[0] in range(10) and neighbor[1] in range(10)):
                continue
            elif board[neighbor[0]][neighbor[1]] == 1:
                continue
            elif neighbor in closed_list:
                continue
            elif newG_score < g_score.get(neighbor, newG_score + 1):
                parent_list[neighbor] = n
                g_score[neighbor] = newG_score
                f_score[neighbor] = newG_score + math.sqrt(abs(neighbor[0] - end[0]) ** 2)  +  math.sqrt(abs(neighbor[1] - end[1]) ** 2)
                if neighbor not in open_list:
                    open_list.append(neighbor)

        open_list.remove(n)
        closed_list.append(n)
        f_score.pop(n)
        g_score.pop(n)


# Just to make the numbers easier on the eyes
def print_board(board):
    for row in board:
        for col in row:
            print(col, end=' ')
        print('')


# Starts the program up
if __name__ == "__main__":
    run()