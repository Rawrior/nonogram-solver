# For the sake of terminology, here's what I'll call a few different things:
#   1. Board = playing area where you actually fill in squares.
#   2. Sequence = a line of filled-in squares
#   3. Encoding = The sequence of numbers describing which sequences are in
#      a given row/col (f.x. "4 6 1")

from board import boardClass


class solverClass:
    DEBUG = False
    rowNum = 0
    colNum = 0
    rows = []
    columns = []
    board = None

    def __init__(self, printDebug=None):
        self.DEBUG = printDebug if printDebug is not None else False

    # TODO: Get some actual logging library, maybe
    def log(self, string):
        if (self.DEBUG):
            print(string)

    def getBoardSizeInput(self):
        self.rowNum = int(input("Enter the number of rows in the puzzle: "))
        self.colNum = int(input("Ener the number of colums in the puzzle: "))
        self.log("Rows: " + str(self.rowNum) + "\nCols: " + str(self.colNum))

    def getRowEncodings(self):
        print("For each row, enter the number sequence, from left to right, "
              "seperated by spaces. Confirm with enter.")
        for i in range(0, self.rowNum):
            self.rows.append(input())

    def getColumnEncodings(self):
        print("\nFor each column, enter the number sequence, from top to"
              "bottom, seperated by spaces. Confirm with enter.")
        for i in range(0, self.colNum):
            self.columns.append(input())

    def initializeBoard(self):
        for i in range(0, len(self.rows)):
            self.rows[i] = list(self.rows[i].split(' '))
            self.rows[i] = [int(x) for x in self.rows[i]]
        for i in range(0, len(self.columns)):
            self.columns[i] = list(self.columns[i].split(' '))
            self.columns[i] = [int(x) for x in self.columns[i]]
        self.board = boardClass(self.rowNum, self.colNum,
                                self.rows, self.columns)

    def printBoard(self):
        print(self.board.getcolNumber(2))
        self.board.printBoard()

    def printGame(self):
        self.board.printGame()
