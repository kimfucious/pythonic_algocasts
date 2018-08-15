import unittest
from exercises.fromlast import from_last
from helpers.linkedlist import Node, LinkedList


@unittest.skip("skip from_last tests")
class FromLastTests(unittest.TestCase):
    def test_from_last_is_callable(self):
        """
        Tests that from_last is callable
        """
        self.assertTrue(callable(from_last))

    def test_from_last(self):
        """
        Tests that from_last returns node n elements from the end of linked list
        """
        l = LinkedList()
        l.insert_last("a")
        l.insert_last("b")
        l.insert_last("c")
        l.insert_last("d")
        l.insert_last("e")
        self.assertEqual(from_last(l, 3), "b")


if __name__ == "__main__":
    unittest.main()
