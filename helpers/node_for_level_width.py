#  This is a helper for the levelwidth exercise.  No need to change anything
#  here.  If you do, it might break the tests.


class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        self.children.append(Node(data))
