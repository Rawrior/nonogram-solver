import pytest
from solver import solverClass
from board import boardClass

solver = None
board = None


@pytest.fixture(scope="function", autouse=True)
def setUpGame():
    global solver
    global boardOne
    global boardTwo
    global capture
    solver = solverClass(True)
    # Test boardOne setup:
    # [ ][X][ ]
    # [ ][X][X]
    # [ ][ ][ ]
    boardOneRowEncodings = [[1], [3], [1]]
    boardOneColEncodings = [[1], [3], [1]]
    boardOne = boardClass(3, 3, boardOneRowEncodings, boardOneColEncodings)
    boardOne.setCell(0, 1, 1)
    boardOne.setCell(1, 1, 1)
    boardOne.setCell(1, 2, 1)

    # Test boardTwo setup:
    # [X][ ][ ]
    # [ ][X][ ]
    # [ ][ ][X]
    boardTwoRowEncodings = [[1, 1], [1], [1, 1]]
    boardTwoColEncodings = [[1, 1], [1], [1, 1]]
    boardTwo = boardClass(3, 3, boardTwoRowEncodings, boardTwoColEncodings)
    boardTwo.setCell(0, 0, 1)
    boardTwo.setCell(1, 1, 1)
    boardTwo.setCell(2, 2, 1)
    yield


def test_log(capsys):
    expected = "test String\n"
    solver.log("test String")
    out, err = capsys.readouterr()
    assert out == expected


def test_printBoard(capsys):
    expectedOne = ("0  1  0  \n"
                   "0  1  1  \n"
                   "0  0  0  \n")
    expectedTwo = ("1  0  0  \n"
                   "0  1  0  \n"
                   "0  0  1  \n")
    boardOne.printBoard()
    out, err = capsys.readouterr()
    assert out == expectedOne

    boardTwo.printBoard()
    out, err = capsys.readouterr()
    assert out == expectedTwo


def test_printGame(capsys):
    expectedOne = ("    1  3  1  \n"
                   "  1 0  1  0  \n"
                   "  3 0  1  1  \n"
                   "  1 0  0  0  \n")
    expectedTwo = ("       1     1  \n"
                   "       1  1  1  \n"
                   "  1  1 1  0  0  \n"
                   "     1 0  1  0  \n"
                   "  1  1 0  0  1  \n")
    boardOne.printGame()
    out, err = capsys.readouterr()
    # assert out == expectedOne

    boardTwo.printGame()
    out, err = capsys.readouterr()
    assert out == expectedTwo
