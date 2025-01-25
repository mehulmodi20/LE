

def is_palindrome(s: str):
    return int(not int(s == s[::-1]))


print(is_palindrome("abc"))
