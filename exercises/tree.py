# --- Directions

# 1) Create a node class.  The __init__() method should accept an argument that
#    gets assigned to the "data" data attribute and initialize an empty list for
#    storing children. The node class should have methods 'add' and 'remove'.
#    The add method should take an argument (e.g. data) and create a new Node in
#    the children list. The remove method will take an argument should delete
#    any node in the children list that has the same data as the argument.
# 2) Create a tree class. The tree should initialize a 'root' data attribute
#    with the initial value of None.
# 3) Implement 'traverse_bf' and 'traverse_df' on the tree class.  Each method
#    should accept a function that gets called with each element in the tree


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        self.children.append(Node(data))

    def remove(self, data):
        """
        Using filter with a lambda to filter the children list
        """
        self.children = list(
            filter(lambda node: node.data != data, self.children))
        #
        # """
        # Using list comprehension to filter the existing children list
        # """
        # self.children = [node for node in self.children if node.data != data]
        #
        # """
        # Using a for loop
        # """
        # for node in self.children:
        #     if node.data == data:
        #         self.children.remove(node)


class Tree:
    def __init__(self):
        self.root = None

    def traverse_bf(self, fn):
        l = [self.root]
        while l:
            node = l.pop(0)
            # l.extend(node.children)
            l = l + node.children
            fn(node)

    def traverse_df(self, fn):
        l = [self.root]
        while l
            node = l.pop(0)
            # There is no method (that I know of) to extend to the front (i.e.
            # prepend) a list of elements to a list
            l = node.children + l
            fn(node)
