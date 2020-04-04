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

    def getRows(self):
        return self.rowEncodings

    def setRows(self, rows):
        self.rowEncodings = rows

    def getColumns(self):
        return self.columnEncodings

    def setColumns(self, columns):
        self.columnEncodings = columns

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
        for row in range(0, len(self.board)):
            for col in range(0, len(self.board[row])):
                print(str(self.board[row][col]) + "  ", end="")
            print()  # Print a newline when a row is done

    def printGame(self):
        # TODO: Like, make this function
        # It should print both the board state and the encodings
        # print(":)")

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

        longestColumn = max(len(x) for x in self.columnEncodings)
        longestRow = max(len(x) for x in self.rowEncodings)

        # print("Longest col: " + str(longestColumn))
        columnNumbers = []
        for i in range(0, longestColumn):
            for j in range(0, len(self.columnEncodings)):
                try:
                    appendNum = self.columnEncodings[j][i]
                    # print("appendNum: " + str(appendNum))
                    columnNumbers.append('{:2}'.format(str(appendNum)))
                except:
                    columnNumbers.append("  ")
        # print("columnNumbers: " + str(columnNumbers))

        printColumns = []
        for i in range(0, longestColumn):
            tempString = ""
            for i in range(0, self.columnAmount):
                tempString = tempString + columnNumbers.pop(0)
            printColumns.append(tempString)
        printColumns = printColumns[::-1]
        # print()
        # for i in range(0, len(printColumns)):
        #     print(printColumns[i])

            #    1 \n
            #   111\n
            # 1 000\n
            # 3 000\n
            # 1 000\n
