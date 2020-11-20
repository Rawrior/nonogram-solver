import pytest


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
def test_get_cell_correct(row, column, expectedOne, expectedTwo, testBoards):
    assert testBoards[0].get_cell(row, column) == expectedOne
    assert testBoards[1].get_cell(row, column) == expectedTwo


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
def test_set_cell_correct(row, column, value1, value2, testBoards):
    testBoards[0].set_cell(row, column, value1)
    testBoards[1].set_cell(row, column, value2)
    assert testBoards[0].get_cell(row, column) == value1
    assert testBoards[1].get_cell(row, column) == value2
