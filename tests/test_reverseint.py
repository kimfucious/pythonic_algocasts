import unittest
from exercises.reverseint import reverse_int


class ReverseIntegerTests(unittest.TestCase):
    def test_reverse_int_exists(self):
        """
        Tests that reverse_int function exists
        """
        self.assertTrue(callable(reverse_int))

    def test_reverse_int_zero(self):
        """
        Tests that reverse_int handles 0 as an input
        """
        self.assertEqual(
            reverse_int(0),
            0
        )

    def test_reverse_flip_pos(self):
        """
        Tests that reverse_int flips a positive number
        """
        self.assertEqual(
            reverse_int(5),
            5
        )
        self.assertEqual(
            reverse_int(15),
            51
        )
        self.assertEqual(
            reverse_int(90),
            9
        )
        self.assertEqual(
            reverse_int(2359),
            9532
        )

    def test_reverse_flip_neg(self):
        """
        reverse_int flips a negative number
        """
        self.assertEqual(
            reverse_int(-5),
            -5
        )
        self.assertEqual(
            reverse_int(-15),
            -51
        )
        self.assertEqual(
            reverse_int(-90),
            -9
        )
        self.assertEqual(
            reverse_int(-2359),
            -9532
        )


if __name__ == "__main__":
    unittest.main()
