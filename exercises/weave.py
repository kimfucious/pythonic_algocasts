# --- Directions
# 1) Complete the task in helpers/queue_for_weave.py
# 2) Implement the "weave" function.  Weave receives two queues as arguments and
#    combines the contents of each into a new, third queue. The third queue
#    should contain the *alterating* content of the two queues.  The function
#    should handle queues of different lengths without inserting "undefined"
#    into the new one. *Do not* access the list inside of any queue, only use
#    the "add", "remove", and "peek" methods.

# --- Example
#    queueOne = Queue()
#    queueOne.add(1)
#    queueOne.add(2)
#    queueTwo = Queue()
#    queueTwo.add("Hi")
#    queueTwo.add("There")
#    q = weave(queueOne, queueTwo)
#    q.remove() # returns 1
#    q.remove() # returns "Hi"
#    q.remove() # returns 2
#    q.remove() # returns "There"

from helpers.queue import Queue


def weave(sourceOne, sourceTwo):
    q3 = Queue()
    while sourceOne.peek() or sourceTwo.peek():
        if sourceOne.peek():
            q3.add(sourceOne.delete())
        if sourceTwo.peek():
            q3.add(sourceTwo.delete())
    return q3
