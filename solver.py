# Method so far:
# 1. Find trivial lines (sum of numbers + spaces = length of row/col)
# 2. Fill out unambiguous sequences (end caps and such)
# 3. Remove spaces where a sequence will not be able to fit.
# 4. Fill spaces that are certain (where sequences will 100% have overlap)
# Rinse and repeat, probably

class Solver:
    from board import boardClass

    DEBUG = True

    # TODO: Get some actual logging library, maybe
    def log(string):
        if (DEBUG):
            print(string)

    # def readNumber(string):
    #     returnList = string.split()
    #     for i in range(len(returnList)):
    #         returnList[i] = int(returnList[i])
    #     return returnList

    # First, let's set up some data, given some input
    rowNum = int(input("Enter the number of rows in the puzzle: "))
    colNum = int(input("Ener the number of colums in the puzzle: "))
    rows = []
    cols = []
    board = boardClass(rowNum, colNum, rows, cols)
    log("Rows: " + str(rowNum) + "\nCols: " + str(colNum))
    board.printBoard()

    print("For each row, enter the number sequence, "
          "from left to right, seperated by spaces. Confirm with enter.")

    for i in range(int(rowNum)):
        rows.append(input())

    print("\nFor each column, enter the number sequence, "
          "from top to bottom, seperated by spaces. Confirm with enter.")
    for i in range(int(colNum)):
        cols.append(input())
