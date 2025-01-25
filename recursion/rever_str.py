#!/usr/bin/env python3.9

"""
Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.
"""


def reverse_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string(s[:-1])


def reverse_string_alt(s):
    return s[::-1]


if __name__ == '__main__':
    print(reverse_string('mehul'))
    print(reverse_string_alt('mehul'))
