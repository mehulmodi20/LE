

def reverse_list(l):
    if len(l) == 0:
        return []
    return [l.pop()] + reverse_list(l)


def reverse_list_2(l):
    return reversed(l)


print(reverse_list([1, 2, 3, 4]))
