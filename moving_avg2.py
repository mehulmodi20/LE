def moving_average(numbers, n=3):
    for i in range(len(numbers) - n + 1):
        print(sum(numbers[i : i + n]) / n, end=" ")


moving_average([40, 30, 50, 46, 39, 44], 3)
print("========")
moving_average([1, 4, 9, 16, 25], n=2)
