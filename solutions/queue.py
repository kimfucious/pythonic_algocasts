# --- Description
# Create a queue data structure.  The queue
# should be a class with methods 'add' and 'remove'.
# Adding to the queue should store an element until
# it is removed
# --- Examples
#     const q = new Q();
#     q.add(1);
#     q.remove(); # returns 1;


class Queue:
    def __init__(self):
        self.data = []

    def add(self, data):
        self.data.insert(0, data)

    def remove(self):
        return self.data.pop()
