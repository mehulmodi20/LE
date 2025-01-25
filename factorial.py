#!/usr/bin/env python3

import sys

n = int(sys.argv[1])
print(n)


def factorial(n):
    res = 1
    if n > 0:
        res = n*factorial(n-1)
    return res


print(factorial(n))
