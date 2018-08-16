# --- Directions
# Given an integer, return an integer that is the reverse ordering of numbers.
# --- Examples
#   reverseInt(15)  # returns 51
#   reverseInt(981) # returns 189
#   reverseInt(500) # returns 5
#   reverseInt(-15) # returns -51
#   reverseInt(-90) # returns -9

from math import copysign


def reverse_int(n):
    return copysign(int((str(abs(n))[::-1])), n)
