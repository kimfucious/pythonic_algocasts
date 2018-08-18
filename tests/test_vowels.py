import unittest
from exercises.vowels import vowels


@unittest.skip("skip vowels tests")
class VowelsTests(unittest.TestCase):
    def test_function_is_callable(self):
        # vowels function is_callable
        self.assertTrue(callable(vowels))

    def test_get_vowels_1(self):
        self.assertEqual(
            vowels("aeiou"),
            5
        )

    def test_get_vowels_2(self):
        self.assertEqual(
            vowels("AEIOU"),
            5
        )

    def test_get_vowels_3(self):
        self.assertEqual(
            vowels("abcdefghijklmnopqrstuvwxyz"),
            5
        )

    def test_get_vowels_4(self):
        self.assertEqual(
            vowels("bcdfghjkl"),
            0
        )


if __name__ == "__main__":
    unittest.main()
