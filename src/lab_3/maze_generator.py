import os
import random
import time

def generate(w = 16, h = 8):
    w = w + 2
    h = h + 2
    maze = [[1 for _ in range(w)] for _ in range(h)]

    def walk(x, y):
        maze[y][x] = 0
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + 2*dx, y + 2*dy
            if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] == 1:
                maze[ny-dy][nx-dx] = 0
                walk(nx, ny)

    walk(random.randrange(0, w, 2), random.randrange(0, h, 2))

    return maze

def print_maze(maze: list[list[int]], pos: tuple[int] = None) -> None:
    os.system('clear')
    print("##"*(len(maze) + 1))
    for idx, row in enumerate(maze):
        if idx == 0:
            print('  '+''.join("##" if i else "  " for i in row))
        elif idx == len(maze) - 2:
            print("##"+''.join("##" if i else "  " for i in row[:-1])+'  ')
        else:
            row_str = ""
            for j, cell in enumerate(row):
                if pos and (j, idx) == pos:
                    row_str += "• "
                elif cell == 1:
                    row_str += "##"
                else:
                    row_str += "  "
            print("##"+row_str)
    time.sleep(.1)