import pytest


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
def test_setCellSequence_correct(coordOne, coordTwo, valueOne, valueTwo, testBoards):
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
