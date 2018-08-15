import unittest
import sys
from io import StringIO
from exercises.pyramid import pyramid


@unittest.skip("skip pyramid tests")
class PyramidTests(unittest.TestCase):
    def test_function_exists(self):
        # pyramid function exists
        self.assertTrue(callable(pyramid))

    def test_pyramid_2(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        pyramid(2)
        # sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), " # \n###\n")

    def test_pyramid_3(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        pyramid(3)
        # sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "  #  \n ### \n#####\n")

    def test_pyramid_4(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        pyramid(4)
        # sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),
                         "   #   \n  ###  \n ##### \n#######\n")


if __name__ == "__main__":
    unittest.main()
