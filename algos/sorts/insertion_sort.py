
'''
Insert sort:

An element is compared to the immediate left element, 
if swapping is performed. The swapped element on the left
also needs to be compared to the all the elements on left.

Time Complexity: O(n^2)
Swapping Complexity: O(n^2)

'''


def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        pos = i
        cur_val = numbers[i]
        while pos > 0 and cur_val < numbers[pos-1]:
            numbers[pos] = numbers[pos-1]
            pos -= 1

        numbers[pos] = cur_val

    return numbers


print(insertion_sort([20, 10, 50, 65, 45, 35]))
