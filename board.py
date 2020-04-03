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

    def getRowNumber(self, index):
        return self.board[index]

    def getcolNumber(self, index):
        out = {}
        for i in range(0, len(self.board)):
            out.append(self.board[i][index])
        return out


    def setCell(self, row, col, value):
        self.board[row][col] = value

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

        # Find sequence with most numbers (per row/col)
        # Copy all the strings to local copies to mess with them.
        # Rows: Pad whole string with spaces (2 per number less than max)
        #       Create new list with every second string char + board row
        # Cols: Turn to horizontal lists. Like so:
        #       Something something...

            #    1 \n
            #   111\n
            # 1 000\n
            # 3 000\n
            # 1 000\n
