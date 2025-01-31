from bisect import insort
from math import ceil
from pathlib import Path
from sys import argv

import numpy as np


from prompt_toolkit import prompt
from prompt_toolkit.key_binding import KeyBindings
from rich.console import Console
from rich.text import Text
import time

def display_list(items):
    console = Console()
    bindings = KeyBindings()

    current_index = 0
    total_items = len(items)

    def show_item(index):
        item = items[index]
        console.clear()
        console.print(Text(f"Did you mean {item[0]}", justify="center"))

    @bindings.add('up')
    def up(event):
        nonlocal current_index
        if current_index > 0:
            current_index -= 1
            show_item(current_index)

    @bindings.add('down')
    def down(event):
        nonlocal current_index
        if current_index < total_items - 1:
            current_index += 1
            show_item(current_index)

    show_item(current_index)
    try:
        while True:
            key = prompt("", key_bindings=bindings, mouse_support=False)
            time.sleep(0.1)
    except KeyboardInterrupt:
        return




def get_levenshtein_distance(a: list[str], b: list[str], a_idx: int = 0, b_idx: int = 0) -> int:
    """
        Depth first levenshtein distance implementation that calculates iteratively
        Distance is defined as the minimum number of insertions (or) deletions (or) substitutions
        which is needed to transform one string into another

        returns early if distance > half the word length of a at any given point
    """
    # distances is a matrix of levenshtein distances where each element ij of distances
    # represents the distance between the first i characters in a and the first j characters in b
    distances = np.zeros((len(a) + 1, len(b) + 1), dtype=int)
    max_distance = ceil(len(a) / 4 * 3)

    distances[:, 0] = np.arange(len(a) + 1)
    distances[0, :] = np.arange(len(b) + 1)
    
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                distances[i, j] = distances[i - 1][j - 1]
            else:
                distances[i, j] = 1 + min(distances[i - 1, j], distances[i, j - 1], distances[i - 1, j - 1])\
    
            if distances[i][j] > max_distance:
                return max_distance + 1

    return distances[len(a), len(b)]


def autocorrect(word: str, dictionary: set[str]) -> list[tuple[str, int]]:
    if word in dictionary:
        return [(word, 0)]
    
    corrections: list[tuple[str, int]] = []

    for w in dictionary:
        insort(corrections, (w, get_levenshtein_distance(word, w)), key=lambda x:x[1])
    
    return corrections


def load_dictionary() -> set[str]:
    with open(Path(__file__).parent / "words.txt") as words_fl:
        words = {word[:-1] for word in words_fl}

    return words


def main() -> None:
    words = load_dictionary()

    if len(argv) == 2:
        input_str = argv[1]
    else:
        input_str = input("Enter a word: ")
    if not (input_str and input_str.isalpha()):
        print("Enter a valid string!")
    corrections = autocorrect(input_str, words)

    print("Use up or down arrows to navigate between suggestions, ctrl+c to exit")
    time.sleep(3)
    display_list(corrections[:100])


if __name__ == "__main__":
    main()