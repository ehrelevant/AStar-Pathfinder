import pygame as game
import math, pprint
import tkinter as tk
from tkinter import messagebox


_WHITE=(255, 255, 255)
_DARK_GRAY=(64, 64, 64)
_BLACK=(0, 0, 0)
_ORANGE=(255, 165, 0)
_GREEN=(0, 255, 0)
_RED=(255, 0, 0)

grid_block = 15

game_speed = 60
clock = game.time.Clock()

neighbor_rel = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

# Get tkinter values
def get_tk():
    size = tuple(map(int, grid_tb.get().split(" ")[::-1]))
    start = tuple(map(int, start_tb.get().split(" ")[::-1]))
    end = tuple(map(int, end_tb.get().split(" ")[::-1]))

    root.quit()
    root.destroy()

    init_pygame(start, end, size=size)
    


def init_pygame(start, end, size=(10, 10)):
    display_width = grid_block * size[0]
    display_height = grid_block * size[1]

    game.init()

    dis = game.display.set_mode((display_width, display_height))
    game.display.set_caption('A* ver_0.1.0')

    game_loop(create_grid(size, dis), start, end, dis)


def create_grid(size, display):
    board = []
    for row in range(size[0]):
        board.append([])
        for col in range(size[1]):
            board[row].append(0)
    display.fill(_WHITE)
    game.display.update()

    return board


def game_loop(board, start, end, dis):
    running=True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running=False

        if game.mouse.get_pressed()[0]: #event.type==pygame.MOUSEBUTTONDOWN
            pos = game.mouse.get_pos()
            col = pos[0] // grid_block
            row = pos[1] // grid_block
            # print(f"x:{col} | y:{row}")
            draw_block(board, dis, col, row, 1)
        elif game.mouse.get_pressed()[2]: #event.type==pygame.MOUSEBUTTONDOWN
            pos = game.mouse.get_pos()
            col = pos[0] // grid_block
            row = pos[1] // grid_block
            # print(f"x:{col} | y:{row}")
            draw_block(board, dis, col, row, 0)

        pressed = game.key.get_pressed()
        if pressed[game.K_r]:
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] in range(2,5):
                        draw_block(board, dis, col, row, 0)

        if pressed[game.K_SPACE]:
            for row in range(len(board)):
                for col in range(len(board[row])):
                    if board[row][col] in range(2,5):
                        draw_block(board, dis, col, row, 0)
            
            result = a_star(board, dis, start, end)
            
            if not result:
                # messagebox.showerror(title='No Path Found', message='There is no path possible in this board')
            else:
                for node in result:
                    draw_block(board, dis, node[1], node[0], 4)


        game.display.flip()
        clock.tick(game_speed)
    game.quit()
    quit()


def a_star(board, dis, start, end):
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
            if newG_score < g_score.get(neighbor, newG_score + 1):
                parent_list[neighbor] = n
                g_score[neighbor] = newG_score
                f_score[neighbor] = newG_score + distance(n, end)
                if neighbor not in open_list:
                    open_list.append(neighbor)

        open_list.remove(n)
        closed_list.append(n)
        for node in open_list:
            draw_block(board, dis, node[1], node[0], 2)
        draw_block(board, dis, n[1], n[0], 3)
        f_score.pop(n)
        g_score.pop(n)

    return False


# The distance formula
def distance(pos_0, pos_1):
    return round(math.sqrt((pos_0[0] - pos_1[0]) ** 2  +  (pos_0[1] - pos_1[1]) ** 2), 2)


def draw_block(board, dis, x, y, set_value):
    board[y][x] = set_value
    if set_value == 0:
        game.draw.rect(dis, _WHITE, [x * grid_block, y * grid_block, grid_block, grid_block])
    elif set_value == 1:
        game.draw.rect(dis, _BLACK, [x * grid_block, y * grid_block, grid_block, grid_block])
    elif set_value == 2:
        game.draw.rect(dis, _GREEN, [x * grid_block, y * grid_block, grid_block, grid_block])
    elif set_value == 3:
        game.draw.rect(dis, _RED, [x * grid_block, y * grid_block, grid_block, grid_block])
    elif set_value == 4:
        game.draw.rect(dis, _ORANGE, [x * grid_block, y * grid_block, grid_block, grid_block])
    game.display.flip()


if __name__ == "__main__":
    root = tk.Tk()
    grid_label = tk.Label(root, text="Grid (Max:40): ")
    grid_tb = tk.Entry(root)
    start_label = tk.Label(root, text="Start: ")
    start_tb = tk.Entry(root)
    end_label = tk.Label(root, text="End: ")
    end_tb = tk.Entry(root)
    submit = tk.Button(root, text="Search", command=get_tk)

    grid_label.grid(row=0, pady=3)
    grid_tb.grid(row=0, column=1, pady=3)
    start_label.grid(row=1, pady=3)
    start_tb.grid(row=1, column=1, pady=3)
    end_label.grid(row=2, pady=3)
    end_tb.grid(row=2, column=1, pady=3)
    submit.grid(columnspan=2, row=3)

    root.update()
    root.mainloop()
    get_tk()
