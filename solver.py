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

    def __init__(self):  # , printDebug=None):
        # self.DEBUG = printDebug if printDebug is not None else False
        pass

    # TODO: Get some actual logging library, maybe
    def log(self, string):
        if (self.DEBUG):
            print(string)

    def get_board_size_input(self):
        try:
            self.rowNum = int(input("Enter the number of rows in the puzzle: "))
            self.colNum = int(input("Ener the number of colums in the puzzle: "))
            self.log("Rows: " + str(self.rowNum) + "\nCols: " + str(self.colNum))
        except ValueError:
            quit("ERROR: Row or column amount must be an integer.")
        if self.rowNum < 1 or self.colNum < 1:
            quit("ERROR: Number of rows or columns cannot be below 1.")

    def get_row_encodings(self):
        print("For each row, enter the number sequence, from left to right, "
              "seperated by spaces. Confirm with enter.")
        for i in range(0, self.rowNum):
            self.rows.append(input())
            # Let's make sure the encoding will fit...
            tempNumbers = list(map(int, self.rows[i].split(" ")))  # Split up the numbers
            tempLength = len(tempNumbers) - 1 + sum(tempNumbers)  # Count the amount of spaces, then add the sum of the numbers
            if tempLength > self.colNum:
                quit(f"ERROR: That encoding will not fit on the board. It takes up {tempLength} spaces, but there are only {self.colNum} available")
            else:
                print("Accepted.")

    def set_column_encodings(self):
        print("\nFor each column, enter the number sequence, from top to "
              "bottom, seperated by spaces. Confirm with enter.")
        for i in range(0, self.colNum):
            self.columns.append(input())
            # Let's make sure the encoding will fit...
            tempNumbers = list(map(int, self.columns[i].split(" ")))  # Split up the numbers
            tempLength = len(tempNumbers) - 1 + sum(tempNumbers)  # Count the amount of spaces, then add the sum of the numbers
            if tempLength > self.rowNum:
                quit(f"ERROR: That encoding will not fit on the board. It takes up {tempLength} spaces, but there are only {self.rowNum} available")
            else:
                print("Accepted.")

    def initialize_board(self):
        for i in range(0, len(self.rows)):
            self.rows[i] = list(self.rows[i].split(' '))
            self.rows[i] = [int(x) for x in self.rows[i]]
        for i in range(0, len(self.columns)):
            self.columns[i] = list(self.columns[i].split(' '))
            self.columns[i] = [int(x) for x in self.columns[i]]
        self.board = boardClass(self.rowNum, self.colNum,
                                self.rows, self.columns)

    def print_board(self):
        self.board.print_board()

    def print_game(self):
        self.board.print_game()
