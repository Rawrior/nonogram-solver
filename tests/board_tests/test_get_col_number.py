import pytest


@pytest.mark.parametrize(
    "column, expectedOne, expectedTwo",
    [
        (0, [0, 0, 0], [1, 0, 0]),
        (1, [1, 1, 0], [0, 0, 0]),
        (2, [0, 1, 0], [1, 0, 1])
    ]
)
def test_get_col_number_correct(column, expectedOne, expectedTwo, testBoards):
    assert testBoards[0].get_col_number(column) == expectedOne
    assert testBoards[1].get_col_number(column) == expectedTwo
