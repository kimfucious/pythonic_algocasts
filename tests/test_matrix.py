import unittest
from exercises.matrix import matrix


# @unittest.skip("skip matrix tests")
class MatrixTests(unittest.TestCase):
    def test_function_exists(self):
        # matrix function exists
        self.assertTrue(callable(matrix))

    def test_matrix_2(self):
        self.assertEqual(
            matrix(2),
            [[1, 2], [4, 3]]
        )

    def test_matrix_3(self):
        self.assertEqual(
            matrix(3),
            [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        )

    def test_matrix_4(self):
        self.assertEqual(
            matrix(4),
            [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
        )


if __name__ == "__main__":
    unittest.main()
