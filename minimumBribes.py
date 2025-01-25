
''' Problem: minimumBribes on Hackerank'''

from typing import List


def minimumBribes(Q):
    moves = 0
    Q = [P-1 for P in Q]
    print(Q)
    for i, P in enumerate(Q):
        print(i, P)
        if P - i > 2:
            print("Too chaotic")
            return
        print(P-1, i)
        print("counting moves")
        for j in range(max(P-1, 0), i):
            if Q[j] > P:
                moves += 1
        print(moves)
        print("=======")
    print(moves)


minimumBribes([2, 1, 5, 3, 4])
