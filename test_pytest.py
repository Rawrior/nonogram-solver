import pytest
from solver import solverClass
from board import boardClass

solver = None
board = None


@pytest.fixture(scope="function", autouse=True)
def setUpGame():
    global solver
    global board
    global capture
    solver = solverClass(True)
    # Test board solution:
    # [ ][X][ ]
    # [X][X][X]
    # [ ][X][ ]
    rowEncodings = ["1", "3", "1"]
    colEncodings = ["1", "3", "1"]
    board = boardClass(3, 3, rowEncodings, colEncodings)
    board.setCell(0, 1, 1)
    board.setCell(1, 0, 1)
    board.setCell(1, 1, 1)
    board.setCell(1, 2, 1)
    board.setCell(2, 1, 1)
    yield


def test_log(capsys):
    expected = "test String\n"
    solver.log("test String")
    out, err = capsys.readouterr()
    assert out == expected


def test_printBoardBlank(capsys):
    expected = ("010\n"
                "111\n"
                "010\n")
    board.printBoard()
    out, err = capsys.readouterr()
    assert out == expected


# For now...
@pytest.mark.xfail
def test_printGameBlank(capsys):
    expected = ("  131\n"
                "1 000\n"
                "3 000\n"
                "1 000\n")
    board.printGame()
    out, err = capsys.readouterr()
    assert out == expected