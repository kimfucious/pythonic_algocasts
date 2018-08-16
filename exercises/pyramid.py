# --- Directions
# Write a function that accepts a positive number N. The function should console
# log a pyramid shape with N levels using the # character.  Make sure the
# pyramid has spaces on both the left *and* right hand sides
# --- Examples
#   pyramid(1)
#       '#'
#   pyramid(2)
#       ' # '
#       '###'
#   pyramid(3)
#       '  #  '
#       ' ### '
#       '#####'


def pyramid(n):
    from math import floor
    midpoint = floor((n*2-1)/2)
    for row in range(0, n):
        step = ""
        for column in range(0, n*2-1):
            if column >= midpoint - row and column <= midpoint + row:
                step += "#"
            else:
                step += " "
        print(step)
