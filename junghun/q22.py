import sys

# 11866 문제 (요세푸스 문제)
from collections import deque

sys.stdin = open("input.txt", "r")
case, gap = map(int, input().split())
yose_deq = deque()
result_arr = list()

for i in range(case):
    yose_deq.append(i + 1)

len_yose = len(yose_deq)

print("<", end="")

for i in range(len_yose):
    yose_deq.rotate(-(gap-1))
    tmp = yose_deq.popleft()
    if i == len_yose - 1:
        print(tmp, end="")
    else:
        print(tmp, end=", ")

print(">")
