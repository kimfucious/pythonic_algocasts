# --- Directions
# Write a function that returns the number of vowels used in a string.  Vowels
# are the characters "a", "e" "i", "o", and "u" and can be upper or lower case.
# --- Examples
#   vowels("Hi There!") --> 3
#   vowels("Why do you ask?") --> 4
#   vowels("Why?") --> 0


def vowels(string):
    """
    Using list comprehension with conditional logic to extract vowels
    """
    vowel_list = [char for char in string.lower() if char in "aeiou"]
    return len(vowel_list)

# def vowels(string):
#     """
#     Using a loop and a list
#     """
#     vowel_list = []
#     for char in string.lower():
#         if char in "aeiou":
#             vowel_list.append(char)
#     return len(vowel_list)

# def vowels(string):
#     """
#     Using a counter
#     """
#     count = 0
#     for char in string.lower():
#         if char in "aeiou":
#             count += 1
#     return count
