

from typing import List
"""

Rotate array to the left by integer d positions

"""


def rotLeft(a: List, d: int):
    new_arr = [0]*(len(a))
    for i in range(len(a)):
        new_arr[i-d] = a[i]
    return new_arr


print(rotLeft([1, 2, 3, 4, 5], 4))
