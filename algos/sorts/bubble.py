

def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] < numbers[j]:
                # print(i, j)
                numbers[i], numbers[j] = numbers[j], numbers[i]
                # print(numbers)
        # print("==========")

    return numbers


print(bubble_sort([5, 20, 10, 50, 65, 45, 35]))
1
