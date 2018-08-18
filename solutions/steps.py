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


def steps(n):
    """
    Using nested loops
    """
    for row in range(0, n):
        step = ""
        for column in range(0, n):
            if column <= row:
                step += "#"
            else:
                step += " "
        print(step)


# def steps(n):
#     """
#     Using a while loop and len(step) instead of column
#     """
#     row = 0
#     step = ""
#     while row != n:
#         if len(step) == n:
#             print(step)
#             row += 1
#             step = ""
#         else:
#             if len(step) <= row:
#                 step += "#"
#             else:
#                 step += " "
