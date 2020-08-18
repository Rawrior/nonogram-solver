import pytest


@pytest.mark.parametrize(
    "column, expectedOne, expectedTwo",
    [
        (2, [0, 1, 0], [1, 0, 1]),
        (1, [1, 1, 0], [0, 0, 0]),
        (0, [0, 0, 0], [1, 0, 0])
    ]
)
def test_getColNumber_correct(column, expectedOne, expectedTwo, testBoards):
    assert testBoards[0].getColNumber(column) == expectedOne
    assert testBoards[1].getColNumber(column) == expectedTwo
