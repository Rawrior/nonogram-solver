def test_print_board_correct(capsys, testBoards):
    expectedOne = ("0  1  0  \n"
                   "0  1  1  \n"
                   "0  0  0  \n")
    expectedTwo = ("1  0  1  \n"
                   "0  0  0  \n"
                   "0  0  1  \n")
    testBoards[0].print_board()
    out, err = capsys.readouterr()
    assert out == expectedOne

    testBoards[1].print_board()
    out, err = capsys.readouterr()
    assert out == expectedTwo


def test_print_game_correct(capsys, testBoards):
    expectedOne = ("    1  3  1  \n"
                   "  1 0  1  0  \n"
                   "  3 0  1  1  \n"
                   "  1 0  0  0  \n")
    expectedTwo = ("             1  \n"
                   "       1  1  1  \n"
                   "  1  1 1  0  1  \n"
                   "     1 0  0  0  \n"
                   "     1 0  0  1  \n")
    testBoards[0].print_game()
    out, err = capsys.readouterr()
    assert out == expectedOne

    testBoards[1].print_game()
    out, err = capsys.readouterr()
    assert out == expectedTwo
