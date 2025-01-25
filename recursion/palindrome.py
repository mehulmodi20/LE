#!/usr/bin/env python3.9
from rever_str import reverse_string
"""
Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise. Remember that a string is a palindrome if it is spelled the same both forward and backward. For example: radar is a palindrome. For bonus points palindromes can also be phrases, but you need to remove the spaces and punctuation before checking. For example: madam i’m adam is a palindrome. Other fun palindromes include:
"""


def is_palindrome(s):
    # make sure to check for case sensitivity.
    new_s = [ch.lower() for ch in s if ch.isalpha()]
    new_s = "".join(new_s)
    return reverse_string(new_s) == new_s


print(is_palindrome("Kanakanak – a town in Alaska"))
print(is_palindrome('Go hang a salami; I’m a lasagna hog.'))
print(is_palindrome('madam i’m adam'))
