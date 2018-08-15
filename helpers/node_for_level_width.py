class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        self.children.append(Node(data))
