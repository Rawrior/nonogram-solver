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
            # and self.rowEncodings == other.rowEncodings
            # and self.columnEncodings == other.columnEncodings
        )

    def get_board(self):
        return self.board

    def set_board(self, board):
        self.board = board

    def get_row_encodings(self):
        return self.rowEncodings

    def set_row_encodings(self, rows):
        self.rowEncodings = rows

    def get_column_encodings(self):
        return self.columnEncodings

    def set_column_encodings(self, columns):
        self.columnEncodings = columns

    def get_row_number(self, index):
        return self.board[index]

    def get_col_number(self, index):
        return [self.board[i][index] for i in range(0, len(self.board))]

    def get_cell(self, row, col):
        return self.board[row][col]

    def set_cell(self, row, col, value):
        self.board[row][col] = value

    def set_cell_sequence(self, coordStart, coordEnd, value):
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
        maxPrintRowLength = (longestRow * 3) + (self.columnAmount * 3) + 1
        for i in range(0, len(self.rowEncodings)):
            tempString = ""
            for j in range(0, len(self.rowEncodings[i])):
                appendNum = self.rowEncodings[i][j]
                tempString = tempString + str(appendNum).rjust(3)
            tempString = tempString + " "
            for j in range(0, len(self.board[i])):
                tempString = tempString + '{:3}'.format(str(self.board[i][j]))
            tempString = tempString.rjust(maxPrintRowLength)
            printRows.append(tempString)

        # GENERATE COLUMNS PRINT
        columnNumbers = []
        for i in range(0, longestColumn):
            for j in range(0, len(self.columnEncodings)):
                try:
                    appendNum = self.columnEncodings[j][i]
                    columnNumbers.append('{:3}'.format(str(appendNum)))
                except IndexError:
                    columnNumbers.append("   ")

        # 3 for the space needed for a number (double-digit and 1 space)
        # 1 for the spacing between the row numbers and the actual board
        colSpacing = longestRow * 3 + 1
        printColumns = []
        for i in range(0, longestColumn):
            tempString = ""
            for i in range(0, self.columnAmount):
                tempString = tempString + columnNumbers.pop(0)
            printColumns.append(tempString.rjust(colSpacing + len(tempString)))
        printColumns = printColumns[::-1]

        for i in range(0, len(printColumns)):
            print(printColumns[i])
        for i in range(0, len(printRows)):
            print(printRows[i])
