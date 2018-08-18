# --- Directions
# Print out the nth entry in the fibonacci series. The fibonacci series is an
# ordering of numbers where each number is the sum of the preceeding two.
# For example, the sequence, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] forms the first
# ten entries of the fibonacci series.
# Example:
#   fib(4) # returns 3
# NOTE: The above sequence starts at 0.  Stephen's tests assert that the
# solutions are working with a series that starts with 1.  I may change these
# later, but for now, assume 1, not zero.


def fib(n):
    """
    Using recursion
    """
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# There are issues with these solutions as the instructions have the Fib series
# starting at zero and Stephen's tests assert that it starts at 1

# def fib(n):
#     result = [0, 1]

#     if n == 1:
#         return 0

#     for index in range(2, n+1):
#         a = result[index - 1]
#         b = result[index - 2]
#         result.append(a + b)

#     return result[-1]


# def fib(n):
#     """
#     Using a while loop and a counter
#     """
#     if n == 1:
#         return 0
#     if n > 0 and n < 3:
#         return 1
#     a = 1
#     b = 1
#     c = 2
#     counter = 3
#     while counter <= n:
#         if counter == n:
#             return c
#         a = b
#         b = c
#         c = a + b
#         counter += 1


print(fib(3))
