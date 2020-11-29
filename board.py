# The board itself. We should have a 2D-"array" for the board, and
# two lists for column and row sequences


class boardClass:
    board = [[]]
    rowEncodings = []
    columnEncodings = []
    rowAmount = 0
    columnAmount = 0

    def __init__(self, rowNum, colNum, rowList, colList):
        self.board = [[0 for i in range(0, colNum)] for i in range(0, rowNum)]
        self.rowEncodings = rowList
        self.columnEncodings = colList
        self.rowAmount = rowNum
        self.columnAmount = colNum

    def __eq__(self, other):
        if not isinstance(other, boardClass):
            return False
        return (
            self.board == other.board
            and self.rowEncodings == other.rowEncodings
            and self.columnEncodings == other.columnEncodings
        )

    def get_board(self):
        return self.board

    def set_board(self, board):
        if not isinstance(board, boardClass):
            raise ValueError("The given parameter is not a board object")
        self.board = board

    def get_row_encodings(self):
        return self.rowEncodings

    def set_row_encodings(self, rows):
        if len(rows) > self.rowAmount:
            raise ValueError("The given row encodings have too many rows")
        else:
            self.rowEncodings = rows

    def get_column_encodings(self):
        return self.columnEncodings

    def set_column_encodings(self, columns):
        if len(columns) > self.columnAmount:
            raise ValueError("The given column encodings have too many columns")
        self.columnEncodings = columns

    def get_row_number(self, index):
        return self.board[index]

    def get_col_number(self, index):
        return [self.board[i][index] for i in range(0, len(self.board))]

    def get_cell(self, row, col):
        return self.board[row][col]

    def set_cell(self, row, col, value):
        if row > self.rowAmount and col > self.columnAmount:
            raise ValueError("Both row and column value are outside of board")
        elif row > self.rowAmount:
            raise ValueError("Row value is outside of board")
        elif col > self.columnAmount:
            raise ValueError("Column value is outside of board")
        else:
            self.board[row][col] = value

    def set_cell_sequence(self, coordStart, coordEnd, value):
        # Errors fall through and are found in set_cell
        for i in range(coordStart[0], coordEnd[0]):
            for j in range(coordStart[1], coordEnd[1]):
                self.set_cell(i, j, value)

    # Prints row-based
    # TODO: Prettify the output a bit (use special characters for blank/filled)
    def print_board(self):
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[row])):
                print(str(self.board[row][col]) + "  ", end="")
            print()  # Print a newline when a row is done

    def print_game(self):
        # TODO: Prettify the output a bit
        # (use special characters for blank/filled)
        longestColumn = max(len(x) for x in self.columnEncodings)
        longestRow = max(len(x) for x in self.rowEncodings)

        # GENERATE ROW PRINT
        printRows = []
        # The longest line to print. Each number is given 2 spaces on each side
        # and each column is given 2 spaces on each side.
        maxPrintRowLength = (longestRow * 3) + (self.columnAmount * 3) + 1
        # For every row...
        for i in range(0, len(self.rowEncodings)):
            tempString = ""
            # For each number in that row encoding...
            for j in range(0, len(self.rowEncodings[i])):
                appendNum = self.rowEncodings[i][j]
                # Appent the number (right-justified in 3 spaces)
                # to the encoding string
                tempString = tempString + str(appendNum).rjust(3)
            # Add a space before the actual playing board
            tempString = tempString + " "
            # For each cell in the row
            for j in range(0, len(self.board[i])):
                # Append the value of the cell, left-adjusted
                tempString = tempString + str(self.board[i][j]).ljust(3)
            # Right-adjust the whole thing
            tempString = tempString.rjust(maxPrintRowLength)
            # Add the string to the rows being printed, then continue with
            # the next row.
            printRows.append(tempString)

        # GENERATE COLUMNS PRINT

        # First, we generate the columns to print
        columnNumbers = []

        # For each index in the longest column (decreasing...)
        # (The first and second -1's are for indexing purposes)
        for i in range(longestColumn - 1, -1, -1):
            # For each column encoding...
            for j in range(0, len(self.columnEncodings)):
                try:
                    # Try to get the number on the (reversed) end and append
                    # it to the list of numbers.
                    appendNum = self.columnEncodings[j][::-1][i]
                    columnNumbers.append(str(appendNum).ljust(3))
                except IndexError:
                    # Otherwise append a blank space
                    columnNumbers.append("   ")

        # Second, print the columns
        # 3 for the space needed for a number (double-digit and 1 space)
        # 1 for the spacing between the row numbers and the actual board
        colSpacing = longestRow * 3 + 1
        printColumns = []
        # For the length of the longest columns...
        for i in range(0, longestColumn):
            tempString = ""
            # For each each column...
            for i in range(0, self.columnAmount):
                # Add the number/space to print
                tempString = tempString + columnNumbers.pop(0)
            # Right-adjust the whole thing by the appropriate amount
            tempString = tempString.rjust(colSpacing + len(tempString))
            # Add to the array of columns to be printed
            printColumns.append(tempString)

        # Add the rows we figured out earlier.
        printColumns.extend(printRows)
        # Then print the whole thing
        for i in range(0, len(printColumns)):
            print(printColumns[i])
