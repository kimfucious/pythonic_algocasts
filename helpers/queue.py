# --- Directions
# Implement a 'peek' method in this Queue class.
# Peek should return the last element (the next
# one to be returned) from the queue *without*
# removing it.


class Queue:
    def __init__(self):
        self.data = []

    def add(self, record):
        self.data.insert(0, record)

    def delete(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            return None

    def peek(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None
