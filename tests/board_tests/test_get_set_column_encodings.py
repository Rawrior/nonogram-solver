def test_setColumnEncodings_correct(testBoards):
    expectedOne = [[3], [1], [3]]
    expectedTwo = [[1, 1], [1, 1], [1]]
    testBoards[0].setColumnEncodings(expectedOne)
    assert testBoards[0].getColumnEncodings() == expectedOne
    testBoards[1].setColumnEncodings(expectedTwo)
    assert testBoards[1].getColumnEncodings() == expectedTwo


def test_getColumnEncodings_correct(testBoards):
    expectedOne = [[1], [3], [1]]
    expectedTwo = [[1], [1], [1, 1]]
    assert testBoards[0].getColumnEncodings() == expectedOne
    assert testBoards[1].getColumnEncodings() == expectedTwo
