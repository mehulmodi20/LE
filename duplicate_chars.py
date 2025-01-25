'''
Given a string eliminate duplicate characters:

aabaabbc --> should return abc
'''


def duplicate_string(s: str):
    new_str = ''
    for ch in s:
        if ch in new_str:
            continue
        else:
            new_str += ch
    return new_str


print(duplicate_string('aabaabbc'))
