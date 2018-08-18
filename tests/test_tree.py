import unittest
from exercises.tree import Node, Tree


@unittest.skip("skip tree node tests")
class TreeNodeTests(unittest.TestCase):
    def test_node_is_callable(self):
        self.assertTrue(callable(Node))

    def test_node_data_attributes(self):
        n = Node("a")
        self.assertEqual(n.data, "a")
        self.assertEqual(len(n.children), 0)

    def test_node_add(self, data="a"):
        n = Node(data)
        n.add("b")
        self.assertEqual(len(n.children), 1)
        self.assertEqual(n.children[0].children, [])

    def test_node_remove(self, data="a"):
        n = Node(data)
        n.add("b")
        self.assertEqual(len(n.children), 1)
        n.remove("b")
        self.assertEqual(len(n.children), 0)


@unittest.skip("skip tree tests")
class TreeTests(unittest.TestCase):

    def test_tree_is_callable_(self):
        self.assertTrue(callable(Tree))

    def test_tree_starts_empty(self):
        t = Tree()
        self.assertEqual(t.root, None)

    def test_tree_traverse_bf(self):
        def fn(node):
            letters.append(node.data)

        letters = []
        t = Tree()
        t.root = Node("a")
        t.root.add("b")
        t.root.add("c")
        t.root.children[0].add("d")

        t.traverse_bf(fn)

        self.assertEqual(letters, ["a", "b", "c", "d"])

    def test_tree_traverse_df(self):
        def fn(node):
            letters.append(node.data)

        letters = []
        t = Tree()
        t.root = Node("a")
        t.root.add("b")
        t.root.add("d")
        t.root.children[0].add("c")

        t.traverse_df(fn)

        self.assertEqual(letters, ["a", "b", "c", "d"])


if __name__ == "__main__":
    unittest.main()
