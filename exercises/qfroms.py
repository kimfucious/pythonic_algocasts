# --- Directions
# Implement a Queue datastructure using two stacks. *Do not* create an array
# inside of the 'Queue' class. Queue should implement the methods 'add',
# 'remove', and 'peek'. For a reminder on what each method does, look back at
# the Queue exercise.
# --- Examples
#     q = Queue()
#     q.add(1)
#     q.add(2)
#     q.peek()  # returns 1
#     q.remove() # returns 1
#     q.remove() # returns 2

from helpers.stack import Stack


class Queue:
    def __init__(self):
        self.stackOne = []
        self.stackTwo = []

    def add(self, data):
        self.stackOne.append(data)

    def peek(self):
        for i in range(0, len(self.stackOne)):
            self.stackTwo.append(self.stackOne.pop())
        peek_item = self.stackTwo[-1]
        for i in range(0, len(self.stackTwo)):
            self.stackOne.append(self.stackTwo.pop())
        return peek_item

    def remove(self):
        for i in range(0, len(self.stackOne)):
            self.stackTwo.append(self.stackOne.pop())
        removed_item = self.stackTwo.pop()
        for i in range(0, len(self.stackTwo)):
            self.stackOne.append(self.stackTwo.pop())
        return removed_item
