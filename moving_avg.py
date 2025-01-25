from collections import deque
import itertools


def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    # print(it)
    d = deque(itertools.islice(it, n - 1))

    d.appendleft(0)
    # print(d)
    s = sum(d)
    for elem in it:
        print(d)
        s += elem - d.popleft()
        # print(s)
        d.append(elem)
        # print(d)
        yield s / float(n)


for m in moving_average([40, 30, 50, 46, 39, 44]):
    print(m, end=" ")

# moving_average([40, 30, 50, 46, 39, 44], 3)
print("========")
for m in moving_average([1, 4, 9, 16, 25], n=2):
    print(m, end=" ")
