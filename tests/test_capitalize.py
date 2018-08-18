import unittest
from exercises.capitalize import capitalize


@unittest.skip("skip capitalize")
class CapitalizeTests(unittest.TestCase):
    def test_function_exists(self):
        # capitalize function exists
        self.assertTrue(callable(capitalize))

    def test_capitalize_1(self):
        self.assertEqual(
            capitalize("hi there, how is it going?"),
            "Hi There, How Is It Going?",
        )

    def test_capitalize_2(self):
        self.assertEqual(
            capitalize("i love breakfast at bill miller bbq"),
            "I Love Breakfast At Bill Miller Bbq",
        )


if __name__ == "__main__":
    unittest.main()
