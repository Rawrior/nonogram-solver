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


@pytest.mark.parametrize(
    "row, column, value, board",
    [
        # 20 is very clearly outside of the board range.
        (0, 20, 1, 0),
        (20, 0, 1, 0),
        (20, 20, 1, 0),
        (0, 20, 0, 0),
        (20, 0, 0, 0),
        (20, 20, 0, 0),
        (0, 20, 1, 1),
        (20, 0, 1, 1),
        (20, 20, 1, 1),
        (0, 20, 0, 1),
        (20, 0, 0, 1),
        (20, 20, 0, 1)
    ]
)
def test_set_cell_incorrect(row, column, value, board, testBoards):
    with pytest.raises(ValueError) as error:
        assert testBoards[board].set_cell(row, column, value)
    if row > testBoards[board].rowAmount and column > testBoards[board].columnAmount:
        assert str(error.value) == "Both row and column value are outside of board"
    elif row > testBoards[board].rowAmount:
        assert str(error.value) == "Row value is outside of board"
    elif column > testBoards[board].columnAmount:
        assert str(error.value) == "Column value is outside of board"
