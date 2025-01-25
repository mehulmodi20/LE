
def square_root(n):
    root = n/2
    for k in range(10):
        root = 1/2 * (root + n/root)
        # root = 1/2

    return root


def sqr_root(n):
    return n**0.5


res = square_root(23.0)
print(res)
res = sqr_root(23.0)
print(res)
