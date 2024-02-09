#!/usr/bin/python3
"""Solution to the N-Queens puzzle"""
import sys


def print_board(board):
    """Prints allocated positions of the queens"""
    for row in board:
        print(row)


def is_safe(board, row, col, n):
    """Checks if a queen can be placed at the given position"""
    # Check the current column on this row
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(n):
    """Solves the N-Queens problem and prints the solutions"""
    board = [[0 for _ in range(n)] for _ in range(n)]

    def helper(row):
        """Recursive helper function to find solutions"""
        if row >= n:
            print_board(board)
            print()
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                helper(row + 1)
                board[row][col] = 0

    helper(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(n)
