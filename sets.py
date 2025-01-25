nfirst_set = int(input())
first_set = set(map(int, input().split()))
nsecond_set = int(input())
second_set = set(map(int, input().split()))

diff = set(sorted(first_set.difference(second_set)) + sorted(second_set.difference(first_set)))

for i in diff:
    print(i)

