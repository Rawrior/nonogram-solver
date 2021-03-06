from board import boardClass


def test_eq_same_boards(testBoards):
    expectedOne = boardClass(3, 3, [[1], [3], [1]], [[1], [3], [1]])
    expectedOne.set_cell(0, 1, 1)
    expectedOne.set_cell(1, 1, 1)
    expectedOne.set_cell(1, 2, 1)

    expectedTwo = boardClass(3, 3, [[1, 1], [1], [1]], [[1], [1], [1, 1]])
    expectedTwo.set_cell(0, 0, 1)
    expectedTwo.set_cell(0, 2, 1)
    expectedTwo.set_cell(2, 2, 1)

    assert expectedOne == testBoards[0]
    assert expectedTwo == testBoards[1]


def test_eq_different_boards(testBoards):
    expectedOne = boardClass(3, 3, [[1], [3], [1]], [[1], [3], [1]])
    expectedTwo = boardClass(3, 3, [[1, 1], [1], [1]], [[1], [1], [1, 1]])

    assert expectedOne != testBoards[0]
    assert expectedTwo != testBoards[1]
