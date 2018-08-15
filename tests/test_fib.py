import unittest
from exercises.fib import fib


@unittest.skip("skip fib tests")
class FibonacciTests(unittest.TestCase):
    def test_fib_exists(self):
        self.assertTrue(callable(fib))

    def test_fib_1(self):
        self.assertEqual(
            fib(1),
            1
        )

    def test_fib_2(self):
        self.assertEqual(
            fib(2),
            1
        )

    def test_fib_3(self):
        self.assertEqual(
            fib(3),
            2
        )

    def test_fib_4(self):
        self.assertEqual(
            fib(4),
            3
        )

    def test_fib_15(self):
        self.assertEqual(
            fib(15),
            63245986
        )


if __name__ == "__main__":
    unittest.main()
