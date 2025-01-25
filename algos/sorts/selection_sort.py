
'''
Selection Sort - 
every element is compared to other element on the right,
in a list and swapping is performed.

Complexity: O(n^2)
Swapping: O(n)

Only algorithm that has O(n) swapping complexity
'''


def selection_sort(numbers):
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[i] >= numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


print(selection_sort([20, 10, 50, 65, 45, 35]))
