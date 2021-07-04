#!/usr/bin/python3
import random
import signal
import time
import sys

FLAG = "shellmates{n0w_d0_1t_w1th_a_64x64_gr1d_huh??}"
SECONDS = 3
BOARD_TEMPLATE = """
╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║
╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
""".strip()


def format_board(board):
    return BOARD_TEMPLATE.replace(".", "{}").format(
        *[[i, " "][i == 0] for row in board for i in row]
    )


def print_board(board):
    print(format_board(board))


class Sudoku:
    def __init__(self, board):
        self.board = [row[:] for row in board]

    def _find_empty_cell(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    return i, j

    def _valid(self, number, position):
        for i in range(len(self.board[0])):
            if self.board[position[0]][i] == number:
                return False

        for i in range(len(board)):
            if self.board[i][position[1]] == number:
                return False

        y = position[0] // 3
        x = position[1] // 3

        for i in range(y * 3, (y + 1) * 3):
            for j in range(x * 3, (x + 1) * 3):
                if self.board[i][j] == number:
                    return False

        return True

    def solve(self):
        cell = self._find_empty_cell()
        if cell is None:
            return True, self.board

        for i in range(1, 10):
            if self._valid(i, cell):
                self.board[cell[0]][cell[1]] = i
                if self.solve()[0]:
                    return True, self.board
                # Backtrack
                self.board[cell[0]][cell[1]] = 0

        return False, None


def generate_board():
    def pattern(r, c):
        return (3 * (r % 3) + r // 3 + c) % 9

    def shuffle(s):
        return random.sample(s, len(s))

    rows = [g * 3 + r for g in shuffle(range(3)) for r in shuffle(range(3))]
    cols = [g * 3 + c for g in shuffle(range(3)) for c in shuffle(range(3))]
    nums = shuffle(range(1, 10))

    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    for i in random.sample(range(81), 81 * 3 // 4):
        board[i // 9][i % 9] = 0

    return board


def alarm_handler(signum, frame):
    sys.stdout.write(f"Too slow!\n")
    sys.stdout.write(f"Try again, and be faster next time! :-)\n")
    sys.stdout.flush()
    sys.exit(0)


signal.signal(signal.SIGALRM, alarm_handler)

sys.stdout.write("Generating puzzle, please stand by...\r")
sys.stdout.flush()

board = generate_board()
_, solution = Sudoku(board).solve()

board = format_board(board)
solution = format_board(solution)

sys.stdout.write("Hello champion! Ready for our today's board?\n")
sys.stdout.write(f"You gotta be quick, {SECONDS} seconds on the counter, let's go!\n")
sys.stdout.write(board + "\n")
sys.stdout.flush()

signal.alarm(SECONDS)

answer = sys.stdin.read(len(BOARD_TEMPLATE)).strip()
if solution == answer:
    sys.stdout.write(f"Well done! {FLAG}\n")
else:
    sys.stdout.write(f"Nah, you can't outsmart :-)\n")

sys.stdout.flush()
