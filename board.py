# The board itself. We should have a 2D-"array" for the board, and
# two lists for column and row sequences


class boardClass:
    board = [[]]
    rows = []
    columns = []

    def __init__(self, rows, columns, rowList, colList):
        self.board = [[0 for i in range(columns)] for i in range(rows)]
        self.rows = rowList
        self.columns = colList

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def getRows(self):
        return self.rows

    def setRows(self, rows):
        self.rows = rows

    def getColumns(self):
        return self.columns

    def setColumns(self, columns):
        self.columns = columns

    # Print row first
    def printBoard(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                print(self.board[row][col], end="")
            print()  # Print a newline when a row is done

    def printGame(self):
        # TODO: Like, make this function
        print(":)")
