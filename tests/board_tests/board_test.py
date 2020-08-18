# Make imports from parent directories possible
import sys
sys.path.append('.')

# Then business as usual
import pytest
from board import boardClass


def test_eq(testBoards):
    expectedOne = boardClass(3, 3, [[1], [3], [1]], [[1], [3], [1]])
    expectedOne.setCell(0, 1, 1)
    expectedOne.setCell(1, 1, 1)
    expectedOne.setCell(1, 2, 1)

    expectedTwo = boardClass(3, 3, [[1, 1], [1], [1]], [[1], [1], [1, 1]])
    expectedTwo.setCell(0, 0, 1)
    expectedTwo.setCell(0, 2, 1)
    expectedTwo.setCell(2, 2, 1)

    assert expectedOne == testBoards[0]
    assert expectedTwo == testBoards[1]


def test_setColumnEncodings(testBoards):
    expectedOne = [[3], [1], [3]]
    expectedTwo = [[1, 1], [1, 1], [1]]
    testBoards[0].setColumnEncodings(expectedOne)
    assert testBoards[0].getColumnEncodings() == expectedOne
    testBoards[1].setColumnEncodings(expectedTwo)
    assert testBoards[1].getColumnEncodings() == expectedTwo


def test_getColumnEncodings(testBoards):
    expectedOne = [[1], [3], [1]]
    expectedTwo = [[1], [1], [1, 1]]
    assert testBoards[0].getColumnEncodings() == expectedOne
    assert testBoards[1].getColumnEncodings() == expectedTwo


@pytest.mark.parametrize(
    "row, expectedOne, expectedTwo",
    [
        (0, [0, 1, 0], [1, 0, 1]),
        (1, [0, 1, 1], [0, 0, 0]),
        (2, [0, 0, 0], [0, 0, 1])
    ]
)
def test_getRowNumber(row, expectedOne, expectedTwo, testBoards):
    assert testBoards[0].getRowNumber(row) == expectedOne
    assert testBoards[1].getRowNumber(row) == expectedTwo


@pytest.mark.parametrize(
    "column, expectedOne, expectedTwo",
    [
        (2, [0, 1, 0], [1, 0, 1]),
        (1, [1, 1, 0], [0, 0, 0]),
        (0, [0, 0, 0], [1, 0, 0])
    ]
)
def test_getColNumber(column, expectedOne, expectedTwo, testBoards):
    assert testBoards[0].getColNumber(column) == expectedOne
    assert testBoards[1].getColNumber(column) == expectedTwo


@pytest.mark.parametrize(
    "row, column, expectedOne, expectedTwo",
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
def test_getCell(row, column, expectedOne, expectedTwo, testBoards):
    assert testBoards[0].getCell(row, column) == expectedOne
    assert testBoards[1].getCell(row, column) == expectedTwo


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
def test_setCell(row, column, value1, value2, testBoards):
    testBoards[0].setCell(row, column, value1)
    assert testBoards[0].getCell(row, column) == value1
    testBoards[1].setCell(row, column, value2)
    assert testBoards[1].getCell(row, column) == value2


@pytest.mark.parametrize(
    "coordOne, coordTwo, valueOne, valueTwo",
    [
        ([0, 0], [0, 2], 1, 0),
        ([1, 0], [1, 2], 1, 0),
        ([2, 0], [2, 2], 1, 0),
        ([0, 0], [2, 0], 1, 0),
        ([0, 1], [2, 1], 1, 0),
        ([0, 2], [2, 2], 1, 0),
        ([2, 0], [2, 0], 1, 0),
        ([1, 0], [1, 2], 1, 0),
        ([1, 2], [1, 2], 1, 0),
        ([2, 0], [2, 1], 1, 0),
        ([0, 0], [2, 2], 1, 0),
        ([2, 2], [0, 0], 1, 0)
    ]
)
def test_setCellSequence(coordOne, coordTwo, valueOne, valueTwo, testBoards):
    testBoards[0].setCellSequence(coordOne, coordTwo, valueOne)
    testBoards[1].setCellSequence(coordOne, coordTwo, valueOne)
    assert assertCells(testBoards[0], coordOne, coordTwo, valueOne)
    assert assertCells(testBoards[1], coordOne, coordTwo, valueOne)

    testBoards[0].setCellSequence(coordOne, coordTwo, valueTwo)
    testBoards[1].setCellSequence(coordOne, coordTwo, valueTwo)
    assert assertCells(testBoards[0], coordOne, coordTwo, valueTwo)
    assert assertCells(testBoards[1], coordOne, coordTwo, valueTwo)


# Helping function for test_setCellSequence
def assertCells(board, coordOne, coordTwo, expectedVal):
    for i in range(coordOne[0], coordTwo[0]):
        for j in range(coordOne[1], coordTwo[1]):
            if board.getCell(i, j) != expectedVal:
                return False
    return True


def test_printBoard(capsys, testBoards):
    expectedOne = ("0  1  0  \n"
                   "0  1  1  \n"
                   "0  0  0  \n")
    expectedTwo = ("1  0  1  \n"
                   "0  0  0  \n"
                   "0  0  1  \n")
    testBoards[0].printBoard()
    out, err = capsys.readouterr()
    assert out == expectedOne

    testBoards[1].printBoard()
    out, err = capsys.readouterr()
    assert out == expectedTwo


def test_printGame(capsys, testBoards):
    expectedOne = ("    1  3  1  \n"
                   "  1 0  1  0  \n"
                   "  3 0  1  1  \n"
                   "  1 0  0  0  \n")
    expectedTwo = ("             1  \n"
                   "       1  1  1  \n"
                   "  1  1 1  0  1  \n"
                   "     1 0  0  0  \n"
                   "     1 0  0  1  \n")
    testBoards[0].printGame()
    out, err = capsys.readouterr()
    assert out == expectedOne

    testBoards[1].printGame()
    out, err = capsys.readouterr()
    assert out == expectedTwo
