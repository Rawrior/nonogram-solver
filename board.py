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

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def getRowEncodings(self):
        return self.rowEncodings

    def setRowEncodings(self, rows):
        self.rowEncodings = rows

    def getColumnEncodings(self):
        return self.columnEncodings

    def setColumnEncodings(self, columns):
        self.columnEncodings = columns

    def getRowNumber(self, index):
        return self.board[index]

    def getColNumber(self, index):
        return [self.board[i][index] for i in range(0, len(self.board))]

    def getCell(self, row, col):
        return self.board[row][col]

    def setCell(self, row, col, value):
        self.board[row][col] = value

    def setCellSequence(self, coordStart, coordEnd, value):
        for i in range(coordStart[0], coordEnd[0]):
            for j in range(coordStart[1], coordEnd[1]):
                self.setCell(i, j, value)


    # Prints row first
    # TODO: Prettify the output a bit (use special characters for blank/filled)
    def printBoard(self):
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[row])):
                print(str(self.board[row][col]) + "  ", end="")
            print()  # Print a newline when a row is done

    def printGame(self):
        # TODO: Like, make this function
        # It should print both the board state and the encodings

        # Find sequence with most numbers (per row/col)
        # Copy all the strings to local copies to mess with them.
        # Rows: Pad whole string with spaces (2 per number less than max)
        #       Create new list with every second string char + board row
        # print(self.columnEncodings)
        longestColumn = max(len(x) for x in self.columnEncodings)
        longestRow = max(len(x) for x in self.rowEncodings)
        # print("Longest column: " + str(longestColumn))

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
            # print(printRows[i])

        # GENERATE COLUMNS PRINT
        # print("Longest col: " + str(longestColumn))
        columnNumbers = []
        for i in range(0, longestColumn):
            for j in range(0, len(self.columnEncodings)):
                try:
                    appendNum = self.columnEncodings[j][i]
                    # print("appendNum: " + str(appendNum))
                    columnNumbers.append('{:3}'.format(str(appendNum)))
                except IndexError:
                    columnNumbers.append("   ")
        # print("columnNumbers: " + str(columnNumbers))

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

            #    1 \n
            #   111\n
            # 1 000\n
            # 3 000\n
            # 1 000\n
