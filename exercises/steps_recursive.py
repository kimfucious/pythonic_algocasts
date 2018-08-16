# --- Directions
# Write a function that accepts a positive number N. The function should console
# log a step shape with N levels using the # character.  Make sure the step has
# spaces on the right hand side!
# --- Examples
#   steps(2)
#       "# "
#       "##"
#   steps(3)
#       "#  "
#       "## "
#       "###"
#   steps(4)
#       "#   "
#       "##  "
#       "### "
#       "####"


def steps(n, row=0, step=""):
    if row == n:
        return
    if len(step) == n:
        print(step)
        row += 1
        steps(n, row)
        return
    if len(step) <= row:
        step += "#"
    else:
        step += " "
    steps(n, row, step)
