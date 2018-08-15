import unittest
import sys
from io import StringIO
from exercises.steps_recursive import steps


# @unittest.skip("skip steps tests")
class StepsTests(unittest.TestCase):
    def test_function_exists(self):
        # steps function exists
        self.assertTrue(callable(steps))

    def test_steps_1(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        steps(1)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "#\n")

    def test_steps_2(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        steps(2)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "# \n##\n")

    def test_steps_3(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        steps(3)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "#  \n## \n###\n")


if __name__ == "__main__":
    unittest.main()
