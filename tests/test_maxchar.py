import unittest
from exercises.maxchar import max_char


@unittest.skip("skip max char tests")
class MaxCharTests(unittest.TestCase):
    def test_function_exists(self):
        # max_char function exists
        self.assertTrue(callable(max_char))

    def test_get_max_char(self):
        # Finds the most frequently used char
        self.assertEqual(
            max_char("abcdefghijklmnaaaaa"),
            "a"
        )

    def test_max_char_with_nums(self):
        # Works with numbers in the string
        self.assertEqual(
            max_char("ab1c1d1e1f1g1"),
            "1"
        )


if __name__ == "__main__":
    unittest.main()
