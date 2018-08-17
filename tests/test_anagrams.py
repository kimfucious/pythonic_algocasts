import unittest
from exercises.anagrams import anagrams


class AnagramsTests(unittest.TestCase):
    def test_anagram_function_exists(self):
        """
        anagrams function exists
        """
        self.assertTrue(callable(anagrams))

    def test_anagrams_1(self):
        self.assertEqual(
            anagrams("hello", "llohe"),
            True
        )

    def test_anagrams_2(self):
        self.assertEqual(
            anagrams("Whoa! Hi!", "Hi Whoa"),
            True
        )

    def test_anagrams_3(self):
        self.assertEqual(
            anagrams("One One", "Two two two"),
            False
        )

    def test_anagrams_4(self):
        self.assertEqual(
            anagrams("A tree, a life, a bench", "A tree, a fence, a yard"),
            False
        )


if __name__ == "__main__":
    unittest.main()
