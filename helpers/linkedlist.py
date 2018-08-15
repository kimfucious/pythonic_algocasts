# --- Directions
# Implement classes Node and Linked Lists
# See 'directions' document


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next_node

    def clear(self):
        self.head = None

    def for_each(self, fn):
        if not self.head:
            return
        node = self.head
        while node:
            fn(node)
            node = node.next_node

    def get_at(self, index):
        counter = 0
        node = self.head
        while node:
            if counter == index:
                return node
            counter += 1
            node = node.next_node
        return None

    def get_first(self):
        return self.head

    def get_last(self):
        if not self.head:
            return None
        node = self.head
        while node:
            if not node.next_node:
                return node
            node = node.next_node

    def insert_first(self, data):
        self.head = Node(data, self.head)

    def insert_at(self, data, index):
        if not self.head:
            self.head = Node(data)
            return
        if index == 0:
            self.head = Node(data, self.head)
            return
        prev = self.get_at(index - 1) or self.get_last()
        prev.next_node = Node(data, prev.next_node)

    def insert_last(self, data):
        last = self.get_last()
        if last:
            last.next_node = Node(data)
        else:
            self.head = Node(data)

    def remove_at(self, index):
        if not self.head:
            return None
        if index == 0:
            self.head = self.head.next_node
            return
        prev = self.get_at(index - 1)
        if not prev or not prev.next_node:
            return
        prev.next_node = prev.next_node.next_node

    def remove_first(self):
        if not self.head:
            return
        self.head = self.head.next_node

    def remove_last(self):
        if not self.head:
            return None
        if not self.head.next_node:
            self.head = None
            return
        prev = self.head
        node = self.head.next_node
        while node.next_node:
            prev = node
            node = node.next_node
        prev.next_node = None

    def size(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next_node
        return counter


def fn(node):
    node.data += 10


l = LinkedList()
l.insert_last(1)
l.insert_last(2)
l.insert_last(3)
l.insert_last(4)
l.for_each(fn)
