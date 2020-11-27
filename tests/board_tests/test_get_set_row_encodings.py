import pytest


def test_set_row_encodings_correct(testBoards):
    expectedZero = [[3], [1], [3]]
    expectedOne = [[1, 1], [1, 1], [1]]
    testBoards[0].set_row_encodings(expectedZero)
    testBoards[1].set_row_encodings(expectedOne)
    assert testBoards[0].get_row_encodings() == expectedZero
    assert testBoards[1].get_row_encodings() == expectedOne


def test_get_row_encodings_correct(testBoards):
    expectedZero = [[1], [3], [1]]
    expectedOne = [[1, 1], [1], [1]]
    assert testBoards[0].get_row_encodings() == expectedZero
    assert testBoards[1].get_row_encodings() == expectedOne


def test_set_row_encodings(testBoards):
    # 5 rows for a 3-row board should definitely be wrong.
    bad_encoding = [[1], [2], [3], [4], [5]]
    with pytest.raises(ValueError) as error:
        assert testBoards[0].set_row_encodings(bad_encoding)
    assert str(error.value) == "The given row encodings have too many rows"

    with pytest.raises(ValueError) as error:
        assert testBoards[1].set_row_encodings(bad_encoding)
    assert str(error.value) == "The given row encodings have too many rows"
