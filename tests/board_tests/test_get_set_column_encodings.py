import pytest


def test_set_column_encodings_correct(testBoards):
    expectedZero = [[3], [1], [3]]
    expectedOne = [[1, 1], [1, 1], [1]]
    testBoards[0].set_column_encodings(expectedZero)
    testBoards[1].set_column_encodings(expectedOne)
    assert testBoards[0].get_column_encodings() == expectedZero
    assert testBoards[1].get_column_encodings() == expectedOne


def test_get_column_encodings_correct(testBoards):
    expectedZero = [[1], [3], [1]]
    expectedOne = [[1], [1], [1, 1]]
    assert testBoards[0].get_column_encodings() == expectedZero
    assert testBoards[1].get_column_encodings() == expectedOne


def test_set_column_encodings(testBoards):
    # 5 columns for a 3-column board should definitely be wrong.
    bad_encoding = [[1], [2], [3], [4], [5]]
    with pytest.raises(ValueError) as error:
        assert testBoards[0].set_column_encodings(bad_encoding)
    assert str(error.value) == "The given column encodings have too many columns"

    with pytest.raises(ValueError) as error:
        assert testBoards[1].set_column_encodings(bad_encoding)
    assert str(error.value) == "The given column encodings have too many columns"
