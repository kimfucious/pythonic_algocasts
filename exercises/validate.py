# --- Directions
# Given a node, validate the binary search tree, ensuring that every node's left
# hand child is less than the parent node's value, and that every node's right
# hand child is greater than the parent
# NOTE:  max and min are built-in functions in Python; however, you can use them
# here eventhough your syntax highlighter might get you thinking otherwise.


def validate(node, min=None, max=None):
    if max is not None and node.data > max:
        return False

    if min is not None and node.data < min:
        return False

    if node.left and not validate(node.left, min, node.data):
        return False

    if node.right and not validate(node.right, node.data, max):
        return False

    return True
