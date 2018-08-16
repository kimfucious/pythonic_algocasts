# --- Directions
# Check to see if two provided strings are anagrams of eachother.
# One string is an anagram of another if it uses the same characters in the same quantity.
# Only consider characters, not spaces or punctuation.
# Consider capital letters to be the same as lower case
# --- Examples
#   anagrams('rail safety', 'fairy tales') --> True
#   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#   anagrams('Hi there', 'Bye there') --> False


def anagrams(stringA, stringB):
    """
    Using regular expression sub() to remove non characters from string
    with helper function. sorted() returns an array, but no need to join
    """
    import re

    def clean_string(string):
        return sorted(re.sub(r"[^\w]", "", string).lower())
    return clean_string(stringA) == clean_string(stringB)


# def anagrams(stringA, stringB):
#     """
#     Using sorted() directly on the strings w/o helper function
#     """
#     import re
#     return sorted(re.sub(r"[^\w]", "", stringA).lower()) == sorted(re.sub(r"[^\w]", "", stringB).lower())


# def anagrams(stringA, stringB):
#     """
#     Using dict comprehension to built character maps
#     with sorted() on the dictionaries
#     """
#     import re
#     char_map_one = {char: stringA.count(
#         char) for char in re.sub(r"[^\w]", "", stringA).lower()}
#     char_map_two = {char: stringB.count(
#         char) for char in re.sub(r"[^\w]", "", stringB).lower()}

#     return sorted(char_map_one) == sorted(char_map_two)
