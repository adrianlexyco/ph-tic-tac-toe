from typing import List

from app.core.models.game import GameMovements

def row_winner(board_size: int, movements: list, player):
    for i in range(0, board_size**2, board_size):
        if all(cell == player for cell in movements[i : i + board_size]):
            return True
    return False


def column_winner(board_size: int, movements: list, player):
    for i in range(board_size):
        if all(movements[j] == player for j in range(i, board_size**2, board_size)):
            return True
    return False


def main_diagonal_winner(board_size: int, movements: list, player):
    if all(movements[i] == player for i in range(0, board_size**2, board_size + 1)):
        return True
    return False


def secondary_diagonal_winner(board_size: int, movements: list, player):
    if all(
        movements[i] == player
        for i in range(board_size - 1, board_size**2 - 1, board_size - 1)
    ):
        return True
    return False


def build_user_board(board_size, movements: List[GameMovements]) -> list:
    board = [None] * (board_size**2)
    for movement in movements:
        board[movement.board_position - 1] = movement.player
    return board
