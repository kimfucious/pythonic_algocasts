# --- Directions
# Check to see if two provided strings are anagrams of eachother.
# One string is an anagram of another if it uses the same characters
# in the same quantity. Only consider characters, not spaces
# or punctuation.  Consider capital letters to be the same as lower case
# --- Examples
#   anagrams('rail safety', 'fairy tales') --> True
#   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
#   anagrams('Hi there', 'Bye there') --> False

import re


def anagrams(stringA, stringB):
    def clean_string(string):
        return "".join(sorted(re.sub(r"[^\w]", "", string).lower()))
    return clean_string(stringA) == clean_string(stringB)
