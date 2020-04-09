# Method so far:
# 1. Find trivial lines (sum of numbers + spaces = length of row/col)
# 2. Fill out unambiguous sequences (end caps and such)
# 3. Remove spaces where a sequence will not be able to fit.
# 4. Fill spaces that are certain (where sequences will 100% have overlap)
# Rinse and repeat, probably

from solver import solverClass
import sys


def main():
    solver = solverClass()
    # Get the board data first
    solver.getBoardSizeInput()
    solver.getRowEncodings()
    solver.getColumnEncodings()
    # Initialize it so we actually have a board
    solver.initializeBoard()

    # solver.printBoard()
    solver.printGame()


if __name__ == "__main__":
    main()
