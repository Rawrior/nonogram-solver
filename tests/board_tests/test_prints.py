def test_printBoard_correct(capsys, testBoards):
    expectedOne = ("0  1  0  \n"
                   "0  1  1  \n"
                   "0  0  0  \n")
    expectedTwo = ("1  0  1  \n"
                   "0  0  0  \n"
                   "0  0  1  \n")
    testBoards[0].printBoard()
    out, err = capsys.readouterr()
    assert out == expectedOne

    testBoards[1].printBoard()
    out, err = capsys.readouterr()
    assert out == expectedTwo


def test_printGame_correct(capsys, testBoards):
    expectedOne = ("    1  3  1  \n"
                   "  1 0  1  0  \n"
                   "  3 0  1  1  \n"
                   "  1 0  0  0  \n")
    expectedTwo = ("             1  \n"
                   "       1  1  1  \n"
                   "  1  1 1  0  1  \n"
                   "     1 0  0  0  \n"
                   "     1 0  0  1  \n")
    testBoards[0].printGame()
    out, err = capsys.readouterr()
    assert out == expectedOne

    testBoards[1].printGame()
    out, err = capsys.readouterr()
    assert out == expectedTwo
