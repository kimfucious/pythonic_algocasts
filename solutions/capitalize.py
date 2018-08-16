# --- Directions
# Write a function that accepts a string.  The function should
# capitalize the first letter of each word in the string then
# return the capitalized string.
# --- Examples
#   capitalize('a short sentence') --> 'A Short Sentence'
#   capitalize('a lazy fox') --> 'A Lazy Fox'
#   capitalize('look, it is working!') --> 'Look, It Is Working!'


def capitalize(string):
    """
    Using the Python str.title() method
    """
    return string.title()

# def capitalize(string):
#     """
#     Using a loop on the string
#     """
#     result = string[0].upper()
#     for index in range(1, len(string)):
#         if string[index-1] == " ":
#             result += string[index].upper()
#         else:
#             result += string[index]
#     return result

# def capitalize(string):
#     """
#     Using a loop on a list split from the string
#     """
#     words = []
#     for word in string.split(" "):
#         words.append(word[0].upper() + word[1:])
#     return " ".join(words)
