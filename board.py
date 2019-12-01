# The board itself. We should have a 2D-"array" for the board, and
# two lists for column and row sequences


class boardClass:
    board = [[]]
    rowEncodings = []
    colEncodings = []

    def __init__(self, rowNum, colNum, rowList, colList):
        self.board = [[0 for i in range(colNum)] for i in range(rowNum)]
        self.rowEncodings = rowList
        self.colEncodings = colList

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def getRows(self):
        return self.rowEncodings

    def setRows(self, rows):
        self.rowEncodings = rows

    def getColumns(self):
        return self.colEncodings

    def setColumns(self, columns):
        self.colEncodings = columns

    # TODO: setCell
    # TODO: setCellSequence

    # Prints row first
    # TODO: Prettify the output a bit ;)
    def printBoard(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                print(self.board[row][col], end="")
            print()  # Print a newline when a row is done

    def printGame(self):
        # TODO: Like, make this function
        # It should print both the board state and the encodings
        print(":)")

        # We need to know the longest encoding of both row and column and save
        # For all rows and cols, we make a local copy to play with
        # if a row/col is shorter than the max length, we pad it with spaces
        # from the left. So a row "3 2" where there is a max length 5, will
        # become "      3 2". Then we can "just" split at every 2nd char and
        # get the resulting list to print.
