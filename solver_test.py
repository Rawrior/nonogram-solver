import pytest
from solver import solverClass

solver = None


@pytest.fixture(scope="function", autouse=True)
def setUpGame():
    global solver
    solver = solverClass(True)


@pytest.mark.skip(reason="Function doesn't exist anymore")
def test_log(capsys):
    expected = "test String\n"
    solver.log("test String")
    out, err = capsys.readouterr()
    assert out == expected
