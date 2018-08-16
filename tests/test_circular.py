import unittest
from exercises.circular import circular
from helpers.linkedlist import Node, LinkedList


# @unittest.skip("skip circular tests")
class CircularTests(unittest.TestCase):
    def test_node_class_exists(self):
        """
        Tests that circular function is callable
        """
        self.assertTrue(callable(circular))

    def test_circular_linked_list_detection(self):
        """
        Tests detection of circular linked lists 
        """
        l = LinkedList()
        a = Node("a")
        b = Node("b")
        c = Node("c")

        l.head = a
        a.next = b
        b.next = c
        c.next = b

        self.assertTrue(circular(l))

    def test_noncircular_linked_list_detection(self):
        """
        Tests detection of non-circular linked lists 
        """
        l = LinkedList()
        a = Node("a")
        b = Node("b")
        c = Node("c")

        l.head = a
        a.next = b
        b.next = c
        c.next = None

        self.assertFalse(circular(l))


if __name__ == "__main__":
    unittest.main()
