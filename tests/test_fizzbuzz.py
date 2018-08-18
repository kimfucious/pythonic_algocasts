import unittest
import sys
import io
from exercises.fizzbuzz import fizzbuzz


@unittest.skip("skip fizzbuzz")
class FizzBuzzTests(unittest.TestCase):
    def test_function_is_callable(self):
        self.assertTrue(callable(fizzbuzz))

    def test_fizz_with_1(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        fizzbuzz(1)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "1\n")

    def test_fizz_with_3(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        fizzbuzz(3)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "1\n2\nfizz\n")

    def test_fizz_with_5(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        fizzbuzz(5)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "1\n2\nfizz\n4\nbuzz\n")

    def test_fizz_with_15(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        fizzbuzz(15)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(
        ), "1\n2\nfizz\n4\nbuzz\nfizz\n7\n8\nfizz\nbuzz\n11\nfizz\n13\n14\nfizzbuzz\n")


if __name__ == "__main__":
    unittest.main()
