# --- Directions
# Given the root node of a tree, return a list where each element is the width
# of the tree at each level.
# --- Example
# Given:
#     0
#   / |  \
# 1   2   3
# |       |
# 4       5
# Answer: [1, 3, 2]


def level_width(root):
    widths = [0]
    l = [root, "end"]
    while len(l) > 1:
        node = l.pop(0)
        if node == "end":
            l.append("end")
            widths.append(0)
        else:
            l = l + node.children
            widths[-1] += 1
    return widths
