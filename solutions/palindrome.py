# --- Directions
# Given a string, return True if the string is a palindrome
# or False if it is not.  Palindromes are strings that
# form the same word if it is reversed. *Do* include spaces
# and punctuation in determining if the string is a palindrome.
# --- Examples:
#   palindrome("abba") === True
#   palindrome("abcdefg") === False


def palindrome(str1):
    return str1 == str1[::-1]
