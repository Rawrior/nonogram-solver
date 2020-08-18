import pytest


@pytest.mark.parametrize(
    "row, expectedOne, expectedTwo",
    [
        (0, [0, 1, 0], [1, 0, 1]),
        (1, [0, 1, 1], [0, 0, 0]),
        (2, [0, 0, 0], [0, 0, 1])
    ]
)
def test_getRowNumber_correct(row, expectedOne, expectedTwo, testBoards):
    assert testBoards[0].getRowNumber(row) == expectedOne
    assert testBoards[1].getRowNumber(row) == expectedTwo
