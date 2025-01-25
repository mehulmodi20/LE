

from typing import List


def isExist(l: List, n):
    midPoint = len(l) // 2
    left = 0
    right = len(l) - 1
    while left <= right:
        if n > l[midPoint]:
            left = midPoint + 1
        else:
            right = midPoint - 1
        print(left, right)
        if l[left] == n or l[right] == n:
            return True
        midPoint = (left + right) // 2
    return False


print(isExist([15, 17, 20, 25, 39, 43, 48, 50], 17))
