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
def test_set_cell_sequence_correct(coordOne, coordTwo, valueOne, valueTwo, testBoards):
    testBoards[0].set_cell_sequence(coordOne, coordTwo, valueOne)
    testBoards[1].set_cell_sequence(coordOne, coordTwo, valueOne)
    assert assertCells(testBoards[0], coordOne, coordTwo, valueOne)
    assert assertCells(testBoards[1], coordOne, coordTwo, valueOne)

    testBoards[0].set_cell_sequence(coordOne, coordTwo, valueTwo)
    testBoards[1].set_cell_sequence(coordOne, coordTwo, valueTwo)
    assert assertCells(testBoards[0], coordOne, coordTwo, valueTwo)
    assert assertCells(testBoards[1], coordOne, coordTwo, valueTwo)


# Helping function for test_set_cell_sequence
def assertCells(board, coordOne, coordTwo, expectedVal):
    for i in range(coordOne[0], coordTwo[0]):
        for j in range(coordOne[1], coordTwo[1]):
            if board.get_cell(i, j) != expectedVal:
                return False
    return True
