# Make imports from parent directories possible
import sys
sys.path.append('.')

# Then business as usual
import pytest
from board import boardClass


@pytest.fixture(scope="function", autouse=True)
def testBoards():
    global boardOne
    global boardTwo
    # Test boardOne initial setup:
    # [ ][X][ ]
    # [ ][X][X]
    # [ ][ ][ ]
    boardOneRowEncodings = [[1], [3], [1]]
    boardOneColEncodings = [[1], [3], [1]]
    boardOne = boardClass(3, 3, boardOneRowEncodings, boardOneColEncodings)
    boardOne.setCell(0, 1, 1)
    boardOne.setCell(1, 1, 1)
    boardOne.setCell(1, 2, 1)

    # Test boardTwo initial setup:
    # [X][ ][X]
    # [ ][ ][ ]
    # [ ][ ][X]
    boardTwoRowEncodings = [[1, 1], [1], [1]]
    boardTwoColEncodings = [[1], [1], [1, 1]]
    boardTwo = boardClass(3, 3, boardTwoRowEncodings, boardTwoColEncodings)
    boardTwo.setCell(0, 0, 1)
    boardTwo.setCell(0, 2, 1)
    boardTwo.setCell(2, 2, 1)
    return boardOne, boardTwo
