#!/usr/bin/python3
from pwn import *
import re

HOST, PORT = "localhost", 1337
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


r = remote(HOST, PORT)
r.recvuntil("let's go!\n")
board = r.recvuntil("╝").decode()
board = [int(i) if i.strip() != "" else 0 for i in re.findall(" . ", board)]
board = [board[i * 9 : (i + 1) * 9] for i in range(9)]

r.info("Got sudoku board:")
print_board(board)

_, solution = Sudoku(board).solve()
solution = format_board(solution)

r.success("Board solved, sending solution...")
print(solution)
r.sendline(solution)

response = r.recvall().decode().strip()
r.success(response)
