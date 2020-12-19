import sys
a, b, c = map(int, sys.stdin.readline().split())


def multiply(i: int, j: int):
    if j == 1:
        return i % c
    else:
        tmp = multiply(i, j // 2)
        if j % 2 == 0:
            return tmp ** 2 % c
        else:
            return tmp ** 2 * i % c


print(multiply(a, b))
