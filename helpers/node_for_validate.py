class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data and self.left:
            self.left.insert(data)
        elif data < self.data:
            self.left = Node(data)
        elif data > self.data and self.right:
            self.right.insert(data)
        elif data > self.data:
            self.right = Node(data)
