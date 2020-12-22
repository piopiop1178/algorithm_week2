import math
import sys

# 1629 문제 (곱셈)
sys.stdin = open("input.txt", "r")
A, B, C = map(int, input().split())


def multi(a, b):
    if b == 1:
        return a % C
    else:
        tmp = multi(a, b // 2)
        if b % 2 == 0:
            return tmp * tmp % C
        else:
            return tmp * tmp * a % C


print(multi(A, B))
