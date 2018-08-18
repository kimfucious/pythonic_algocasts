import unittest
from exercises.palindrome import palindrome


@unittest.skip("skip palindromes")
class PalindromeTests(unittest.TestCase):
    def test_function_is_callable(self):
        # Palindrome function is_callable
        self.assertTrue(callable(palindrome))

    def test_palindrome(self):
        # "aba" is a palindrome
        self.assertEqual(
            palindrome("aba"),
            True
        )

    def test_palindrome_two(self):
        # "1000000001" is a palindrome
        self.assertEqual(
            palindrome("1000000001"),
            True
        )

    def test_palindrome_three(self):
        # "pennep" is a palindrome
        self.assertEqual(
            palindrome("pennep"),
            True
        )

    def test_not_a_palindrome(self):
        # " aba" is not a palindrome
        self.assertEqual(
            palindrome(" aba"),
            False
        )

    def test_not_a_palindrome_two(self):
        # "aba " is not a palindrome
        self.assertEqual(
            palindrome("aba "),
            False
        )

    def test_not_a_palindrome_three(self):
        # "greetings" is not a palindrome
        self.assertEqual(
            palindrome("greetings"),
            False
        )

    def test_not_a_palindrome_four(self):
        # "Fish hsif" is not a palindrome
        self.assertEqual(
            palindrome("Fish hsif"),
            False
        )


if __name__ == "__main__":
    unittest.main()
