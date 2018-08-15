import unittest
from exercises.bst import Node


@unittest.skip("skip bst tests")
class BinarySearchTreeTests(unittest.TestCase):
    def test_node_class_exists(self):
        """
        Test that Node class exists and is callable
        """
        self.assertTrue(callable(Node))

    def test_insert_node(self):
        """
        Test insertion of node into binary search tree
        """
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(17)
        self.assertEqual(node.left.data, 5)
        self.assertEqual(node.right.data, 15)
        self.assertEqual(node.right.right.data, 17)

    def test_contains_returns_node(self):
        """
        Test that contains method returns correct node based on given value
        """
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(20)
        node.insert(0)
        node.insert(-5)
        node.insert(3)
        three = node.left.left.right
        self.assertEqual(node.contains(3), three)

    def test_contains_returns_none(self):
        """
        Test that contains method returns none if value not found 
        """
        node = Node(10)
        node.insert(5)
        node.insert(15)
        node.insert(20)
        node.insert(0)
        node.insert(-5)
        node.insert(3)
        self.assertEqual(node.contains(9999), None)


if __name__ == "__main__":
    unittest.main()
