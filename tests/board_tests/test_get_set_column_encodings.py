def test_set_column_encodings_correct(testBoards):
    expectedOne = [[3], [1], [3]]
    expectedTwo = [[1, 1], [1, 1], [1]]
    testBoards[0].set_column_encodings(expectedOne)
    testBoards[1].set_column_encodings(expectedTwo)
    assert testBoards[0].get_column_encodings() == expectedOne
    assert testBoards[1].get_column_encodings() == expectedTwo


def test_get_column_encodings_correct(testBoards):
    expectedOne = [[1], [3], [1]]
    expectedTwo = [[1], [1], [1, 1]]
    assert testBoards[0].get_column_encodings() == expectedOne
    assert testBoards[1].get_column_encodings() == expectedTwo
