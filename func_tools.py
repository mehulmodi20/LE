from functools import partial


def square(n):
    return n*n


print(*map(partial(square), [1, 2, 3, 4]))
