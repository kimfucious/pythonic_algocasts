import unittest
from exercises.reversestring import reverse


@unittest.skip("skip reverse string")
class ReverseStringTests(unittest.TestCase):
    def test_function_is_callable(self):
        """
        Tests that reverse function is_callable
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
