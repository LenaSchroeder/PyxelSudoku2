"""Sudoku Game"""

# import packages and functions defined in board
import random
from copy import deepcopy
from typing import List, NewType

from sudoku_app import App
import pyxel
from board import Board, rowsValid, cols_vald, board_valid, update_board


def generate_random_puzzle():
    pass


# Check if the board is valid.





def format_board(current_board):
    return """
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
---------------------
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
---------------------
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
""".format(
        *[val if val else " " for row in current_board for val in row]
    )


def fill_board(puzzle):
    spots = iter(puzzle)
    puzzle_board = [[int(next(spots)) for _ in range(9)] for _ in range(9)]
    return puzzle_board  # change from a string to a list of list of ints


def read_line_from_puzzlefile(file):
    # Read sudoku data
    f = open(file)
    text = f.read()
    # Get one of the puzzles and its corresponding solution
    lines = text.splitlines()
    line_number = random.randint(0, len(lines))
    return lines[line_number]


def format_puzzle(line):
    line = line.strip()
    puzzle, solution = line.split(",")
    return puzzle, solution


game_won = False

line = read_line_from_puzzlefile("sudoku.csv")
puzzle, solution = format_puzzle(line)

# Make a board structure to fill in the data with.
empty_board = [[0 for _ in range(9)] for _ in range(9)]

# Fill Board with puzzle data
puzzle_board = fill_board(puzzle)
solution_board = fill_board(solution)

rowsValid(solution_board)

cols_vald(solution_board)

pyxel.init(156, 183, caption="Sudoku Game")

# change board
selected_value = 1
cell_selected = (0, 0)

update_board(puzzle_board, 4, 4, 8)

pyxel.cls(3)
pyxel.text(1, 1, "8", 0)

is_valid = True
pyxel.load("my_resource.pyxres", True, True)
image = pyxel.image(0)

app = App(puzzle_board, solution_board, is_valid, cell_selected, selected_value, game_won)

# start the game #
pyxel.mouse(True)
pyxel.run(app.update, app.draw)

print("That was fun, why don't we play again?")
