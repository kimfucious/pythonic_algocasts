import unittest
from exercises.weave import weave
from helpers.queue_for_weave import Queue


@unittest.skip("skip weave")
class WeaveStringTests(unittest.TestCase):
    def test_peek_exists(self):
        # queues have a peek function
        q = Queue()
        self.assertTrue(callable(q.peek))

    def test_peek(self):
        # peek returns, but does not remove, the first value
        q = Queue()
        q.add(1)
        q.add(2)
        self.assertEqual(
            q.peek(),
            1
        )
        self.assertEqual(
            q.peek(),
            1
        )
        self.assertEqual(
            q.delete(),
            1
        )
        self.assertEqual(
            q.delete(),
            2
        )

    def test_weave_exists(self):
        # weave is a function
        self.assertTrue(callable(weave))

    def test_weave(self):
        one = Queue()
        one.add(1)
        one.add(2)
        one.add(3)
        one.add(4)
        two = Queue()
        two.add("one")
        two.add("two")
        two.add("three")
        two.add("four")

        res = weave(one, two)
        self.assertEqual(res.delete(), 1)
        self.assertEqual(res.delete(), "one")
        self.assertEqual(res.delete(), 2)
        self.assertEqual(res.delete(), "two")
        self.assertEqual(res.delete(), 3)
        self.assertEqual(res.delete(), "three")
        self.assertEqual(res.delete(), 4)
        self.assertEqual(res.delete(), "four")
        self.assertEqual(res.delete(), None)
        # self.assertRaises(IndexError, res.delete())


if __name__ == "__main__":
    unittest.main()
