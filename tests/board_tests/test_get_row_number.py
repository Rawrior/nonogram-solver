import pytest


@pytest.mark.parametrize(
    "row, expectedOne, expectedTwo",
    [
        (0, [0, 1, 0], [1, 0, 1]),
        (1, [0, 1, 1], [0, 0, 0]),
        (2, [0, 0, 0], [0, 0, 1])
    ]
)
def test_get_row_number_correct(row, expectedOne, expectedTwo, testBoards):
    assert testBoards[0].get_row_number(row) == expectedOne
    assert testBoards[1].get_row_number(row) == expectedTwo
