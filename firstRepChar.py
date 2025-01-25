
from collections import Counter


def get_first_rep_char(s: str):
    s_count = Counter(s)
    s_map = {}
    for index, val in enumerate(s):
        if s_map.get(val):
            return val
        else:
            s_map[val] = 1


print(get_first_rep_char('geeksforgeeks'))
