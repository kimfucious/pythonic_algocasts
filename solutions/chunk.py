# --- Directions
# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size
# --- Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]


def chunk(array, size):
    """
    Using while until the array is empty
    Emptying out the array using del 
    """
    chunked = []
    while len(array) > 0:
        chunked.append(array[0:size])
        del array[0:size]
    return chunked

# def chunk(array, size):
#     """
#     Using while with an index counter
#     """
#     chunked = []
#     index = 0
#     while index < len(array):
#         chunked.append(array[index:index+size])
#         index += size
#     return chunked

# def chunk(array, size):
#     """
#     Using interation DOES NOT WORK!
#     """
#     chunked = []
#     for element in array:
#         last = chunked[len(chunked) - 1]
#         if not last or len(last) == size:
#             chunked.append([element])
#         else:
#             last.append(element)
#     return chunked
