# --- Directions
# Write a function that accepts an integer, n, and returns a n x n spiral matrix.
# --- Examples
#   matrix(2)
#     [[1, 2],
#     [4, 3]]
#   matrix(3)
#     [[1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]]
#  matrix(4)
#     [[1,   2,  3, 4],
#     [12, 13, 14, 5],
#     [11, 16, 15, 6],
#     [10,  9,  8, 7]]


def matrix(n):
    """
    Need to create a list of n x n filled with None to avoid 'IndexError: list
    index out of range' issues when using this technique Also note the +1s and
    -1s on the ranges, as the second argument in a range is non-inclusive. There
    are other ways to do this, but they make my head explode:
    https://rosettacode.org/wiki/Spiral_matrix#Python
    """
    spiral = [[None] * n for j in range(n)]
    start_col, start_row = 0, 0
    end_col, end_row = n-1, n-1
    counter = 1

    while start_col <= end_col and start_row <= end_row:
        for index in range(start_row, end_col+1):
            spiral[start_row][index] = counter
            counter += 1
        start_row += 1

        for index in range(start_row, end_row+1):
            spiral[index][end_col] = counter
            counter += 1
        end_col -= 1

        for index in range(end_col, start_col-1, -1):
            spiral[end_row][index] = counter
            counter += 1
        end_row -= 1

        for index in range(end_row, start_row-1, -1):
            spiral[index][start_col] = counter
            counter += 1
        start_col += 1

    return spiral
