import unittest
from exercises.reversestring import reverse


class ReverseStringTests(unittest.TestCase):
    def test_function_exists(self):
        """
        Tests that reverse function exists
        """
        self.assertTrue(callable(reverse))

    def test_reverse(self):
        """
        Tests that reverse can reverse a string
        """
        self.assertEqual(
            reverse("apple"),
            "elppa"
        )


if __name__ == "__main__":
    unittest.main()
