# Yeah this just does A* I guess
import math
import pprint

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
    # print_board(def_board)
    while True:
        #start_pos = tuple(map(int, input('Starting position: ').split(' ')))  # Formats to: [x, y]
        #end_pos = tuple(map(int, input('Ending position: ').split(' ')))
        start_pos = (2, 2)      # Uses samples for faster testing
        end_pos = (2, 9)

        a_star(def_board, start_pos, end_pos)
        break


def a_star(board, start, end):
    open_list = [start]
    closed_list = []

    parent = {start: None}

    # f-score = g-score + h-score
    g_score = {start: 0}

    start_h = math.sqrt(abs(start[0] - end[0]) ** 2)  +  math.sqrt(abs(start[1] - end[1]) ** 2)
    # Kinda like 2D Vector distance calculation
    f_score = {start: start_h}  # f(start_h) = h(start_h) + g(0)


    while len(open_list) > 0:
        temp_dict = {}
        for pos in open_list:
            if pos in f_score.keys():
                temp_dict[pos] = f_score[pos]

        n = min(temp_dict, key = temp_dict.get)     # Gets the key with the minimum f-score


        if n == end:
            path = [n]
            while n in parent.keys():
                n = parent[n]
                path.insert(0, n)
            path.pop(0)
            pprint.pprint(f_score)
            
            
            for square in path:
                board[square[0]][square[1]] = 2
            print_board(board)
            break


        # Finds all neighbors in list; There's probably a simpler way to do this but for now this is it
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
                neighbor_list.append(tuple(neighbor_pos))


        for neighbor in neighbor_list:
            newG_score = g_score[n] + 1

            if board[neighbor[0]][neighbor[1]] == 1:
                continue
            elif neighbor in closed_list:
                continue
            elif neighbor in open_list:
                if g_score[neighbor] > newG_score:
                    parent[neighbor] = n
                    g_score[neighbor] = newG_score
                    heuristic = math.sqrt(abs(neighbor[0] - end[0]) ** 2)  +  math.sqrt(abs(neighbor[1] - end[1]) ** 2)
                    f_score[neighbor] = newG_score + heuristic
            else:
                open_list.append(neighbor)
                parent[neighbor] = n
                g_score[neighbor] = newG_score
                heuristic = math.sqrt(abs(n[0] - end[0]) ** 2)  +  math.sqrt(abs(n[1] - end[1]) ** 2)
                f_score[neighbor] = newG_score + heuristic
        
        open_list.remove(n)
        closed_list.append(n)


def print_board(board):     # Honestly just makes it easier to the eyes
    for row in board:
        for col in row:
            print(col, end=' ')
        print('')


if __name__ == "__main__":
    run()