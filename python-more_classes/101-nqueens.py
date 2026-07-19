#!/usr/bin/python3
"""Solves the N queens puzzle using backtracking."""
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed at (row, col).

    Args:
        board: List where board[i] is the column of the queen in row i.
        row: The row to check.
        col: The column to check.

    Returns:
        True if no other queen attacks this position.
    """
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve(n, row, board, solutions):
    """Recursively place queens row by row.

    Args:
        n: The size of the board.
        row: The current row to place a queen in.
        board: Current partial solution (column per row).
        solutions: List collecting all complete solutions.
    """
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append(col)
            solve(n, row + 1, board, solutions)
            board.pop()


def main():
    """Parse arguments and print all N queens solutions."""
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

    solutions = []
    solve(n, 0, [], solutions)
    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])


if __name__ == "__main__":
    main()
