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


def pyramid(n, row=0, step=""):
    from math import floor
    if row == n:
        return
    if len(step) == n*2-1:
        print(step)
        row += 1
        return pyramid(n, row)
    midpoint = floor((n*2-1)/2)
    if len(step) >= midpoint - row and len(step) <= midpoint + row:
        step += "#"
    else:
        step += " "
    pyramid(n, row, step)
