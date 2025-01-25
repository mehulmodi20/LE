from collections import Counter
(n, m) = map(int, input().split())
numbers = Counter(map(int, input().split()))
like = set(map(int, input().split()))
dislike = set(map(int, input().split()))
happiness = 0
for num in numbers:
    if num in like:
        happiness += numbers[num]
    elif num in dislike:
        happiness -= numbers[num]
print(happiness)
