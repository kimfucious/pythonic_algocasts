import unittest
from helpers.node_for_level_width import Node
from exercises.levelwidth import level_width


@unittest.skip("skip level width tests")
class LevelWidthTests(unittest.TestCase):
    def test_level_width_is_callable(self):
        """
        Tests that level width is callable
        """
        self.assertTrue(callable(level_width))

    def test_level_width_1(self):
        """
        Tests the return of number of nodes at widest point
        """
        root = Node(0)
        root.add(1)
        root.add(2)
        root.add(3)
        root.children[0].add(4)
        root.children[2].add(5)
        self.assertEqual(level_width(root), [1, 3, 2])

    def test_level_width_2(self):
        """
        Tests the return of number of nodes at widest point
        """
        root = Node(0)
        root.add(1)
        root.children[0].add(1)
        root.children[2].add(3)
        root.children[0].children.add(4)
        self.assertEqual(level_width(root), [1, 1, 2, 1])


if __name__ == "__main__":
    unittest.main()
