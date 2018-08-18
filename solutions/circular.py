# --- Directions
# Given a linked list, return True if the list is circular, False if it is not.
# --- Examples
#   l = LinkedList()
#   a = Node('a')
#   b = Node('b')
#   c = Node('c')
#   l.head = a
#   a.next = b
#   b.next = c
#   c.next = b
#   circular(l) # True


def circular(l):
    slow = l.get_at(0)
    fast = l.get_at(0)

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
