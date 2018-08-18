# --- Directions
# Print out the nth entry in the fibonacci series. The fibonacci series is an
# ordering of numbers where each number is the sum of the preceeding two. For
# example, the sequence, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] forms the first ten
# entries of the fibonacci series. Example: fib(4) # returns 3
# NOTE: The above sequence starts at 0.  Stephen's tests assert that the
# solutions are working with a series that starts with 1.  I may change these
# later, but for now, assume 1, not zero.
# NOTE:  I couldn't come up with a name for the inner function of the memoize
# function, so I named it george.


def memoize(fn):
    cache = {}

    def george(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = fn(*args)
            return cache[args]
    return george


@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
