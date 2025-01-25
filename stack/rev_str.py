from stack import Stack


def reverse_string(s):
    stack = Stack()
    for ch in s:
        stack.push(ch)
    rev_str = ''
    while stack.size() > 0:
        rev_str += stack.pop()
    return rev_str


def alt_rev_string(s):
    return s[::-1]


print(reverse_string("mehul"))
print(alt_rev_string("mehul"))
