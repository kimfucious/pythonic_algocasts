#  This is a helper for the qfroms exercise.  No need to change anything here.
#  If you do, it might break the tests.


class Stack:
    def __init__(self):
        self.data = []

    def push(self, record):
        self.data.append(record)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]
