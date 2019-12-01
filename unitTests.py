import unittest
import io
import sys
from solver import solverClass

class TestPrintMethods(unittest.TestCase):
    def setUp(self):
        self.solver = Solver(True)

    def test_log(self):
        capture = io.StringIO()
        sys.stdout = capture
        solver.log("test string")
        sys.stdout = sys.__stdout__
        self.assertEqual("test String", capture.getValue())

# Make the tests runnable in console.
if __name__ == '__main__':
    unittest.main()
