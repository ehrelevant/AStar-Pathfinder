import pygame as game
import math, pprint
import tkinter as tk

WHITE=(255,255,255)
DARK_GRAY=(64,64,64)
BLACK=(0,0,0)
ORANGE=(255,165,0)

# Get tkinter values
def get_tk():
    """size = tuple(grid_tb.get().split(" ")[::-1])
    start = tuple(start_tb.get().split(" ")[::-1])
    end = tuple(end_tb.get().split(" ")[::-1])

    root.quit()
    root.destroy()"""
    size = (9, 9)
    start = (0, 0)
    end = (9, 9)
    init_pygame(start, end, size=size)


def init_pygame(start, end, size=(10, 10)):
    grid_block = 20
    display_width = grid_block * size[0]
    display_height = grid_block * size[1]

    game.init()

    dis = game.display.set_mode((display_width, display_height))
    game.display.set_caption('A* ver_0.1.0')

    clock = game.time.Clock()
    gameSpeed=60

    create_grid(size, dis, grid_block)


def create_grid(size, display, block_unit):
    board = []
    for row in range(size[0]):
        board.append([])
        for col in range(size[1]):
            game.draw.rect(display, WHITE, [row * block_unit, col * block_unit, block_unit, block_unit])
            board[row].append(0)
    game.display.update()
    
    pprint.pprint(board)
    return board


if __name__ == "__main__":
    """root = tk.Tk()
    grid_label = tk.Label(root, text="Grid (Max:20): ")
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
    root.mainloop()"""
    get_tk()
