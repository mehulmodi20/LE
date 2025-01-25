
'''
Notes: 
1. data must be in sorted order.
2. Complexity: O(log n)
'''


def bin_search(arr, key):
    L = 0
    R = len(arr)-1

    while L <= R:
        mid = (L+R)//2
        if arr[mid] == key:
            return True
        elif arr[mid] < key:
            L = mid + 1
        elif arr[mid] > key:
            R = mid - 1
    return False


print(bin_search([15, 21, 45, 60, 70, 80], 80))
