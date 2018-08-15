import unittest
from exercises.midpoint import midpoint
from helpers.linkedlist import Node, LinkedList


@unittest.skip("skip midpoint tests")
class MidpointTests(unittest.TestCase):
    def test_function_exists(self):
        # midpoint function exists
        self.assertTrue(callable(midpoint))

    def test_midpoint_odd(self):
        l = LinkedList()
        l.insertLast("a")
        l.insertLast("b")
        l.insertLast("c")
        self.assertEqual(
            midpoint((l).data),
            "b"
        )


if __name__ == "__main__":
    unittest.main()
