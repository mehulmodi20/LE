from collections import OrderedDict
nwords = int(input())
ordered_count = OrderedDict()
for _ in range(nwords):
    word = input()
    if ordered_count.get(word, 0):
        ordered_count[word] += 1
    else:
        ordered_count[word] = 1
print(len(ordered_count.keys()))
print(' '.join([str(i) for i in ordered_count.values()]))
