#  --- Directions
#  Given a string, return a new string with the reversed order of characters
#  --- Examples
#    reverse('apple') # returns 'leppa'
#    reverse('hello') # returns 'olleh'
#    reverse('Greetings!') # returns '!sgniteerG'


def reverse(string):
    """
    Using a slice with a stride of -1 to reverse the string directly 
    """
    return string[:: -1]

# def reverse(string):
#     """
#     Using reduce with a lambda right on the string
#     No need to split into an array in Python
#     But you gotta import reduce from functools to use it
#     """
#     from functools import reduce
#     return reduce((lambda acc, curr: curr+acc), string)


# def reverse(string):
#     """
#     Using a loop
#     """
#     reversed_string = ""
#     for char in string:
#         reversed_string = char + reversed_string
#     return reversed_string
