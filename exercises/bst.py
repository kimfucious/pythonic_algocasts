# --- Directions
# 1) Implement the Node class to create a binary search tree.  The __init__()
#    method should take an argument of "data" and should initialize data
#    attributes: "data", "left", and "right".  "left" and "right" should have
#    initial values of None.
# 2) Implement the "insert" method for the Node class.  Insert should accept an
#    argument "data", then create an insert a new node at the appropriate
#    location in the tree.
# 3) Implement the "contains" method for the Node class.  Contains should accept
#    a "data" argument and return the Node in the tree with the same value.


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def contains(self, data):
        if self.data == data:
            return self
        if self.left and data < self.data:
            return self.left.contains(data)
        elif self.right and data > self.data:
            return self.right.contains(data)
        else:
            return None

    def insert(self, data):
        if self.left and data < self.data:
            self.left.insert(data)
        elif data < self.data:
            self.left = Node(data)

        if self.right and data > self.data:
            self.right.insert(data)
        elif data > self.data:
            self.right = Node(data)
