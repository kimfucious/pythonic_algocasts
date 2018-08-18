import unittest
from exercises.sorting import bubble_sort, selection_sort, merge, merge_sort


@unittest.skip("skip sorting")
class SortingTests(unittest.TestCase):
    def test_bubble_sort_is_callable(self):
        self.assertTrue(callable(bubble_sort))

    def test_selection_sort_is_callable(self):
        self.assertTrue(callable(selection_sort))

    def test_merge_function_is_callable(self):
        self.assertTrue(callable(merge))

    def test_merge_sort_is_callable(self):
        self.assertTrue(callable(merge_sort))

    def get_list(self):
        return [100, -40, 500, -124, 0, 21, 7]

    def get_sorted_list(self):
        return [-124, -40, 0, 7, 21, 100, 500]

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.get_list()), self.get_sorted_list())

    def test_selection_sort(self):
        self.assertEqual(selection_sort(self.get_list()),
                         self.get_sorted_list())

    def test_merge_function(self):
        left = [1, 10]
        right = [2, 8, 12]
        self.assertEqual(merge(left, right), [1, 2, 8, 10, 12])

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.get_list()), self.get_sorted_list())


if __name__ == "__main__":
    unittest.main()
