import random
import maze_generator
import os
import time

from functools import cache

def index_bound(x: int, y: int, length: int) -> bool:
    return 0 <= x < length and 0 <= y < length

def move(x: int, y: int, direction: str) -> tuple[int]:
    if direction == 'right':
        return x, y + 1
    elif direction == 'down':
        return x + 1, y
    elif direction == 'left':
        return x, y - 1
    elif direction == 'up':
        return x - 1, y

def solve(maze: list[list[int]]) -> list[tuple[int]]:
    length = len(maze)
    end = (length - 2, length - 2)
    visited = set()
    moves = [(0, 0)]

    def dfs(x: int, y: int, path: list[tuple[int]]) -> list[tuple[int]]:
        if (x, y) == end:
            return path[:]
        visited.add((x, y))
        directions = ['right', 'down', 'left', 'up']
        random.shuffle(directions)
        for direction in directions:
            nx, ny = move(x, y, direction)
            if index_bound(nx, ny, length) and maze[ny][nx] == 0:
                maze_generator.print_maze(maze, (nx, ny))
                if (nx, ny) not in visited:
                    new_path = path + [(nx, ny)]
                    solution = dfs(nx, ny, new_path)
                    if solution:
                        maze_generator.print_maze(maze, (nx, ny))
                        return solution
                        
        if index_bound(nx, ny, length) and maze[ny][nx] == 0:
            maze_generator.print_maze(maze, (nx, ny))
        return None

    return dfs(1, 1, moves)

def main() -> None:
    size = int(input("Enter maze side length: "))
    maze = maze_generator.generate(size, size)
    maze_generator.print_maze(maze)
    solution = solve(maze)
    if solution:
        print("Solution found")
    else:
        print("No solution found")

if __name__ == "__main__":
    main()
