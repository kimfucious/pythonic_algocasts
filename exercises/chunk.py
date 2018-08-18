# --- Directions
# Given a list and chunk size, divide the list into multiple nested lists within
# a list where each nested list is of length size
# --- Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]


def chunk(l, size):
    """
    Using while until the list is empty Emptying out the list using del 
    """
    chunked = []
    while len(l) > 0:
        chunked.append(l[0:size])
        del l[0:size]
    return chunked

# def chunk(l, size):
#     """
#     Using while with an index counter
#     """
#     chunked = []
#     index = 0
#     while index < len(l):
#         chunked.append(l[index:index+size])
#         index += size
#     return chunked

# def chunk(l, size):
#     """
#     Using interation DOES NOT WORK!
#     """
#     chunked = []
#     for element in l:
#         last = chunked[len(chunked) - 1]
#         if not last or len(last) == size:
#             chunked.append([element])
#         else:
#             last.append(element)
#     return chunked
