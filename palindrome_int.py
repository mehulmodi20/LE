from typing import List


def main(n, integers: List):
    print(all([int(integers[i]) >= 0 for i in range(n)]) and any(
        [integers[i] == ''.join(reversed(integers[i])) for i in range(n)]))


if __name__ == '__main__':
    nintegers = int(input())
    numbers = input().split()
    main(nintegers, numbers)
