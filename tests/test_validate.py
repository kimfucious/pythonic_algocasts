import unittest
from helpers.node_for_validate import Node
from exercises.validate import validate


@unittest.skip("skip validate binary search tree tests")
class ValidateTests(unittest.TestCase):
    def test_function_is_callable(self):
        # validate function is_callable
        self.assertTrue(callable(validate))

    def test_validate_valid_bst(self):
        n = Node(10)
        n.insert(5)
        n.insert(15)
        n.insert(0)
        n.insert(20)
        self.assertTrue(validate(n))

    def test_validate_invalid_bst(self):
        n = Node(10)
        n.insert(5)
        n.insert(15)
        n.insert(0)
        n.insert(20)
        n.left.left.right = Node(999)
        self.assertFalse(validate(n))


if __name__ == "__main__":
    unittest.main()
