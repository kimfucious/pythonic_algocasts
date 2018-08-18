import unittest
from exercises.chunk import chunk


@unittest.skip("skip chunk tests")
class ChunkTests(unittest.TestCase):
    def test_chunk_function_is_callable(self):
        self.assertTrue(callable(chunk))

    def test_chunk_10_2(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(
            chunk(arr, 2),
            [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        )

    def test_chunk_3_1(self):
        arr = [1, 2, 3]
        self.assertEqual(
            chunk(arr, 1),
            [[1], [2], [3]]
        )

    def test_chunk_5_3(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(
            chunk(arr, 3),
            [[1, 2, 3], [4, 5]]
        )

    def test_chunk_13_5(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(
            chunk(arr, 5),
            [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]]
        )


if __name__ == "__main__":
    unittest.main()
