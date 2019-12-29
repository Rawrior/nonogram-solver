import unittest
import io
import sys
from solver import solverClass
from board import boardClass


class TestConsolePrintMethods(unittest.TestCase):
    def gameDataSetup(self):
        # Test board solution:
        # [ ][X][ ]
        # [X][X][X]
        # [ ][X][ ]
        self.rowEncodings = ["1", "3", "1"]
        self.colEncodings = ["1", "3", "1"]
        self.solver = solverClass(True)
        self.board = boardClass(3, 3, self.rowEncodings, self.colEncodings)

    def setUp(self):
        self.gameDataSetup()
        self.capture = io.StringIO()
        sys.stdout = self.capture

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_log(self):
        # We have to include the \n as the log uses a regular print()
        self.solver.log("test String")
        self.assertEqual("test String\n", self.capture.getvalue())

    def test_printBoardBlank(self):
        expected = ("000\n"
                    "000\n"
                    "000\n")
        self.board.printBoard()
        self.assertEqual(expected, self.capture.getvalue())

    # For now...
    @unittest.expectedFailure
    def test_printGameBlank(self):
        expected = ("  131\n"
                    "1 000\n"
                    "3 000\n"
                    "1 000\n")
        self.board.printGame()
        self.assertEqual(expected, self.capture.getvalue())


# Make the tests runnable in console.
if __name__ == '__main__':
    unittest.main()
