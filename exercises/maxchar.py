# --- Directions
# Given a string, return the character that is most commonly used in the string.
# --- Examples
# max_char("abcccccccd") === "c"
# max_char("apple 1231111") === "1"


def max_char(string):
    """
    Getting fancy with max() and lambda!
    https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    """
    char_map = {char: string.count(char) for char in string}
    return max(char_map, key=(lambda key: char_map[key]))

# def max_char(string):
#     """
#     Using dictionary comprehension to create char_map
#     """
#     max_count = 0
#     max_key = ""
#     char_map = {char: string.count(char) for char in string}
#     for key in char_map:
#         if char_map[key] > max_count:
#             max_count = char_map[key]
#             max_key = key

#     return max_key

# def max_char(string):
#     """
#     Using for/in to create char_map dictionary
#     """
#     char_map = {}
#     max_count = 0
#     max_key = ""
#     for char in string:
#         if char in char_map:
#             char_map[char] += 1
#         else:
#             char_map[char] = 0
#     for key in char_map:
#         if char_map[key] > max_count:
#             max_count = char_map[key]
#             max_key = key

#     return max_key


max_char("abcdefghijklmnaaaaazzzzzzzzzzzzzzzzzzzzzzzzzzz")
