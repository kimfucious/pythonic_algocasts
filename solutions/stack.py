# --- Directions
# Create a stack data structure.  The stack should be a class with methods
# 'push', 'pop', and 'peek'.  Adding an element to the stack should store it
# until it is removed. If a list is empty return None for peek and pop
# --- Examples
#   s = Stack();
#   s.pop() # returns None
#   s.peek() # returns None
#   s.push(1)
#   s.push(2)
#   s.pop() # returns 2
#   s.pop() # returns 1


class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        # If statement prevents error when popping an empty list
        if self.data:
            return self.data.pop()
        else:
            return None

    def peek(self):
        # If statement prevents error when trying to get non existent value
        if self.data:
            return self.data[-1]
        else:
            return None
