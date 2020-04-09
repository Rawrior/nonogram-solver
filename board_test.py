import pytest
from board import boardClass

board = None


@pytest.fixture(scope="function", autouse=True)
def setUpGame():
    global boardOne
    global boardTwo
    global capture
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
    # [X][ ][X]
    # [ ][ ][ ]
    # [ ][ ][X]
    boardTwoRowEncodings = [[1, 1], [1], [1]]
    boardTwoColEncodings = [[1], [1], [1, 1]]
    boardTwo = boardClass(3, 3, boardTwoRowEncodings, boardTwoColEncodings)
    boardTwo.setCell(0, 0, 1)
    boardTwo.setCell(0, 2, 1)
    boardTwo.setCell(2, 2, 1)
    yield


def test_setColumnEncodings():
    expectedOne = [[3], [1], [3]]
    expectedTwo = [[1, 1], [1, 1], [1]]
    boardOne.setColumnEncodings(expectedOne)
    assert boardOne.getColumnEncodings() == expectedOne
    boardTwo.setColumnEncodings(expectedTwo)
    assert boardTwo.getColumnEncodings() == expectedTwo


def test_getColumnEncodings():
    expectedOne = [[1], [3], [1]]
    expectedTwo = [[1], [1], [1, 1]]
    assert boardOne.getColumnEncodings() == expectedOne
    assert boardTwo.getColumnEncodings() == expectedTwo


@pytest.mark.parametrize(
    "row, expected1, expected2",
    [
        (0, [0, 1, 0], [1, 0, 1]),
        (1, [0, 1, 1], [0, 0, 0]),
        (2, [0, 0, 0], [0, 0, 1])
    ]
)
def test_getRowNumber(row, expected1, expected2):
    assert boardOne.getRowNumber(row) == expected1
    assert boardTwo.getRowNumber(row) == expected2


@pytest.mark.parametrize(
    "column, expected1, expected2",
    [
        (2, [0, 1, 0], [1, 0, 1]),
        (1, [1, 1, 0], [0, 0, 0]),
        (0, [0, 0, 0], [1, 0, 0])
    ]
)
def test_getColNumber(column, expected1, expected2):
    assert boardOne.getColNumber(column) == expected1
    assert boardTwo.getColNumber(column) == expected2


@pytest.mark.parametrize(
    "row, column, expected1, expected2",
    [
        (0, 0, 0, 1),
        (0, 1, 1, 0),
        (0, 2, 0, 1),
        (1, 0, 0, 0),
        (1, 1, 1, 0),
        (1, 2, 1, 0),
        (2, 0, 0, 0),
        (2, 1, 0, 0),
        (2, 2, 0, 1)
    ]
)
def test_getCell(row, column, expected1, expected2):
    assert boardOne.getCell(row, column) == expected1
    assert boardTwo.getCell(row, column) == expected2


@pytest.mark.parametrize(
    "row, column, value1, value2",
    [
        (0, 0, 1, 0),
        (0, 1, 0, 1),
        (0, 2, 1, 0),
        (1, 0, 1, 1),
        (1, 1, 0, 1),
        (1, 2, 0, 1),
        (2, 0, 1, 1),
        (2, 1, 1, 1),
        (2, 2, 1, 0)
    ]
)
def test_setCell(row, column, value1, value2):
    boardOne.setCell(row, column, value1)
    assert boardOne.getCell(row, column) == value1
    boardTwo.setCell(row, column, value2)
    assert boardTwo.getCell(row, column) == value2


def test_printBoard(capsys):
    expectedOne = ("0  1  0  \n"
                   "0  1  1  \n"
                   "0  0  0  \n")
    expectedTwo = ("1  0  1  \n"
                   "0  0  0  \n"
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
    expectedTwo = ("             1  \n"
                   "       1  1  1  \n"
                   "  1  1 1  0  1  \n"
                   "     1 0  0  0  \n"
                   "     1 0  0  1  \n")
    boardOne.printGame()
    out, err = capsys.readouterr()
    assert out == expectedOne

    boardTwo.printGame()
    out, err = capsys.readouterr()
    assert out == expectedTwo
