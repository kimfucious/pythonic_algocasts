import unittest
from exercises.stack import Stack


@unittest.skip("skip stack tests")
class StackTests(unittest.TestCase):
    def test_stack_is_callable(self):
        """
        Test that Stack class is callable
        """
        self.assertTrue(callable(Stack))

    def test_stack_add_remove(self):
        """
        Test that stack can add and remove items
        """
        s = Stack()
        s.push(1)
        self.assertEqual(s.pop(), 1)
        s.push(2)
        self.assertEqual(s.pop(), 2)

    def test_stack_follows_filo(self):
        """
        Test that stack follows first in, last out 
        """
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_stack_peek(self):
        """
        Test that peek returns the first element but doesn't remove it 
        """
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.peek(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.peek(), 1)
        self.assertEqual(s.pop(), 1)


if __name__ == "__main__":
    unittest.main()
