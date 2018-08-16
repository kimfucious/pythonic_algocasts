import unittest
from exercises.linkedlist import LinkedList, Node


class LinkedListTests(unittest.TestCase):
    def test_node_class_exists(self):
        """
        Tests that Node class exists and is callable
        """
        self.assertTrue(callable(Node))

    def test_linkedlist_class_exists(self):
        """
        Tests that LinkedList class exists and is callable
        """
        self.assertTrue(callable(LinkedList))

    def test_node_creation(self):
        """
        Tests that Node class has properties of 'data' and 'next'
        """
        node = Node("a", "b")
        self.assertEqual(node.data, "a")
        self.assertEqual(node.next, "b")


# @unittest.skip("Clear List Tests")
class ClearTests(unittest.TestCase):
    def test_clear(self):
        """
        Test that a list is emptied
        """
        l = LinkedList()
        self.assertEqual(l.size(), 0)
        l.insert_first(1)
        l.insert_first(1)
        l.insert_first(1)
        l.insert_first(1)
        self.assertEqual(l.size(), 4)
        l.clear()
        self.assertEqual(l.size(), 0)


# @unittest.skip("ForEach Tests")
class ForEachTests(unittest.TestCase):
    def test_for_each(self):
        """
        Test that a transform runs on each node 
        """
        def fn(node):
            node.data += 10
        l = LinkedList()
        l.insert_last(1)
        l.insert_last(2)
        l.insert_last(3)
        l.insert_last(4)
        l.for_each(fn)
        self.assertEqual(l.get_at(0).data, 11)
        self.assertEqual(l.get_at(1).data, 12)
        self.assertEqual(l.get_at(2).data, 13)
        self.assertEqual(l.get_at(3).data, 14)


# @unittest.skip("For In Tests")
class ForInTests(unittest.TestCase):
    def test_for_in_loop_on_linked_list(self):
        """
        Tests that a for of loop will work on a linked list
        """
        l = LinkedList()
        l.insert_last(1)
        l.insert_last(2)
        l.insert_last(3)
        l.insert_last(4)

        for node in l:
            node.data += 10

        self.assertEqual(l.get_at(0).data, 11)
        self.assertEqual(l.get_at(1).data, 12)
        self.assertEqual(l.get_at(2).data, 13)
        self.assertEqual(l.get_at(3).data, 14)


# @unittest.skip("Get At Tests")
class GetAtTests(unittest.TestCase):
    def test_get_at_out_of_bounds(self):
        """
        Tests the return of None from an index that is out of bounds
        """
        l = LinkedList()
        self.assertEqual(l.get_at(10), None)

    def test_get_at(self):
        """
        Tests the return of a node from a given index
        """
        l = LinkedList()
        l.insert_last(1)
        l.insert_last(2)
        l.insert_last(3)
        l.insert_last(4)
        self.assertEqual(l.get_at(0).data, 1)
        self.assertEqual(l.get_at(1).data, 2)
        self.assertEqual(l.get_at(2).data, 3)
        self.assertEqual(l.get_at(3).data, 4)


# @unittest.skip("Get First Tests")
class GetFirstTests(unittest.TestCase):
    def test_get_first(self):
        """
        Tests that the first node of a list is returned
        """
        l = LinkedList()
        l.insert_first(1)
        self.assertEqual(l.get_first().data, 1)
        l.insert_first(2)
        self.assertEqual(l.get_first().data, 2)


# @unittest.skip("Get Last Tests")
class GetLastTests(unittest.TestCase):
    def test_get_last(self):
        """
        Tests that the last node of a list is returned
        """
        l = LinkedList()
        l.insert_first(2)
        self.assertEqual(l.get_last().data, 2)
        self.assertEqual(l.get_last().next, None)
        l.insert_first(1)
        self.assertEqual(l.get_last().data, 2)
        self.assertEqual(l.get_last().next, None)


# @unittest.skip("Insert At Tests")
class InsertAtTests(unittest.TestCase):
    def test_insert_at_0_on_empty_list(self):
        """
        Tests insertion of node on empty list
        """
        l = LinkedList()
        l.insert_at("hi", 0)
        self.assertEqual(l.get_first().data, "hi")

    def test_insert_at_0_non_empty_list(self):
        """
        Tests for insertion of node at index 0 on non-empty list
        """
        l = LinkedList()
        l.insert_last("a")
        l.insert_last("b")
        l.insert_last("c")
        l.insert_at("hi", 0)
        self.assertEqual(l.get_at(0).data, "hi")
        self.assertEqual(l.get_at(1).data, "a")
        self.assertEqual(l.get_at(2).data, "b")
        self.assertEqual(l.get_at(3).data, "c")

    def test_insert_at_middle_index(self):
        """
        Test for insertion of node at index in the middle of a list
        """
        l = LinkedList()
        l.insert_last("a")
        l.insert_last("b")
        l.insert_last("c")
        l.insert_last("d")
        l.insert_at("hi", 2)
        self.assertEqual(l.get_at(0).data, "a")
        self.assertEqual(l.get_at(1).data, "b")
        self.assertEqual(l.get_at(2).data, "hi")
        self.assertEqual(l.get_at(3).data, "c")
        self.assertEqual(l.get_at(4).data, "d")

    def test_insert_at_last_index(self):
        """
        Tests for insertion of node at the end of a list
        """
        l = LinkedList()
        l.insert_last("a")
        l.insert_last("b")
        l.insert_at("hi", 2)
        self.assertEqual(l.get_at(0).data, "a")
        self.assertEqual(l.get_at(1).data, "b")
        self.assertEqual(l.get_at(2).data, "hi")

    def test_insert_at_out_of_bounds(self):
        """
        Tests that node is inserted at the end of a list when index is out of bounds
        """
        l = LinkedList()
        l.insert_last("a")
        l.insert_last("b")
        l.insert_at("hi", 30)
        self.assertEqual(l.get_at(0).data, "a")
        self.assertEqual(l.get_at(1).data, "b")
        self.assertEqual(l.get_at(2).data, "hi")


# @unittest.skip("Insert First Tests")
class InsertFirstTests(unittest.TestCase):

    def test_insert_first(self):
        """
        Tests appending a node to the start of the list
        """
        l = LinkedList()
        l.insert_first(1)
        self.assertEqual(l.head.data, 1)
        l.insert_first(2)
        self.assertEqual(l.head.data, 2)


# @unittest.skip("Remove First Tests")
class RemoveFirstTests(unittest.TestCase):
    def test_remove_first_size_1(self):
        """
        Tests the removal of first node in list when list has one node
        """
        l = LinkedList()
        l.insert_first("a")
        l.remove_first()
        self.assertEqual(l.size(), 0)
        self.assertEqual(l.get_first(), None)

    def test_remove_first_size_3(self):
        """
        Tests the removal of first node in list when list has three nodes 
        """
        l = LinkedList()
        l.insert_first("c")
        l.insert_first("b")
        l.insert_first("a")
        l.remove_first()
        self.assertEqual(l.size(), 2)
        self.assertEqual(l.get_first().data, "b")
        l.remove_first()
        self.assertEqual(l.size(), 1)
        self.assertEqual(l.get_first().data, "c")


# @unittest.skip("Remove Last Tests")
class RemoveLastTests(unittest.TestCase):
    def test_remove_last_empty(self):
        """
        Tests the return of None when run on empty list
        """
        l = LinkedList()
        self.assertEqual(l.remove_last(), None)

    # @unittest.skip("skip")
    def test_remove_last_1(self):
        """
        Tests the removal of last node in a list with one node 
        """
        l = LinkedList()
        l.insert_first("a")
        l.remove_last()
        self.assertEqual(l.head, None)

    # @unittest.skip("skip")
    def test_remove_last_2(self):
        """
        Tests the removal of last node in a list with two nodes 
        """
        l = LinkedList()
        l.insert_first("b")
        l.insert_first("a")
        l.remove_last()
        self.assertEqual(l.size(), 1)
        self.assertEqual(l.get_last().data, "a")
        self.assertEqual(l.get_last().next, None)

    # @unittest.skip("skip")
    def test_remove_last_3(self):
        """
        Tests the removal of last node in a list with three nodes 
        """
        l = LinkedList()
        l.insert_first("c")
        l.insert_first("b")
        l.insert_first("a")
        l.remove_last()
        self.assertEqual(l.size(), 2)
        self.assertEqual(l.get_last().data, "b")


# @unittest.skip("Insert Last Tests")
class InsertLastTests(unittest.TestCase):
    def test_insert_last(self):
        """
        Tests adding a node to the end of a list
        """
        l = LinkedList()
        l.insert_first("a")
        l.insert_last("b")
        self.assertEqual(l.size(), 2)
        self.assertEqual(l.get_last().data, "b")


# @unittest.skip("Remove At Tests")
class RemoveAtTests(unittest.TestCase):
    def test_remove_at_out_of_bounds(self):
        """ 
        Tests for return of None when called on index that is out of bounds
        """
        l = LinkedList()
        l.insert_first("a")
        l.remove_at(1)
        self.assertEqual(l.remove_at(1), None)

    def test_remove_at_first_node(self):
        """
        Tests removal of first node
        """
        l = LinkedList()
        l.insert_last(1)
        l.insert_last(2)
        l.insert_last(3)
        l.insert_last(4)
        self.assertEqual(l.get_at(0).data, 1)
        l.remove_at(0)
        self.assertEqual(l.get_at(0).data, 2)

    def test_remove_at_given_index(self):
        """
        Tests for removal of node at given index
        """
        l = LinkedList()
        l.insert_last(1)
        l.insert_last(2)
        l.insert_last(3)
        l.insert_last(4)
        self.assertEqual(l.get_at(1).data, 2)
        l.remove_at(1)
        self.assertEqual(l.get_at(1).data, 3)


# @unittest.skip("Size Tests")
class SizeTests(unittest.TestCase):
    def test_size(self):
        """
        Tests that the size of a linked list is returned
        """
        l = LinkedList()
        self.assertEqual(l.size(), 0)
        l.insert_first(1)
        l.insert_first(1)
        l.insert_first(1)
        l.insert_first(1)
        self.assertEqual(l.size(), 4)


if __name__ == "__main__":
    unittest.main()
