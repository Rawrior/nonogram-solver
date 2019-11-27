import unittest
import io
import sys
import solver


class TestPrintMethods(unittest.TestCase):
    def test_log(self):
        capture = io.StringIO()
        sys.stdout = capture
        solver.log("test string")
        sys.stdout = sys.__stdout__
        self.assertEqual("test String", capture.getValue())


if __name__ == '__main__':
    unittest.main()
