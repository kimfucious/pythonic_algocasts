import unittest
from exercises.queue import Queue


@unittest.skip("skip queue")
class QueueTests(unittest.TestCase):
    def test_fib_exists(self):
        self.assertTrue(callable(Queue))

    def test_add(self):
        # can add elements to a queue
        q = Queue()
        q.add(1)
        q.add(2)
        self.assertEqual(
            len(q.data),
            2
        )

    def test_remove(self):
        # can remove elements from a queue
        q = Queue()
        q.add(1)
        q.add(2)
        q.add(3)
        q.remove()
        q.remove()
        q.remove()
        self.assertEqual(len(q.data), 0)

    def test_order(self):
        # Order of elements is maintained
        q = Queue()
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(q.remove(), 1)
        self.assertEqual(q.remove(), 2)
        self.assertEqual(q.remove(), 3)


if __name__ == "__main__":
    unittest.main()
