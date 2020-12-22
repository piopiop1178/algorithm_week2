

# n1, test1 = int(sys.stdin.readline()), sorted(list(map(int, sys.stdin.readline().split())))
# n2, test2 = int(sys.stdin.readline()), sorted(list(map(int, sys.stdin.readline().split())))
# n3, test3 = int(sys.stdin.readline()), sorted(list(map(int, sys.stdin.readline().split())))
#
#
# def histogram(n: int, hist: list):
#     start = hist[0]
#     last = len(hist) - 1
#     mid = hist.index(min(hist))
#     area = (mid - start) + (last - mid)
#
#     if mid > start:
#         histogram(hist[start:mid])
#     else:
#         histogram(hist[])

import sys

while True:
    tmp = list(map(int, sys.stdin.readline().split()))
    n = tmp[0]
    if n == 0:
        break

    top = [0] + tmp[1:] + [0]

    stack = [0]
    area = 0
    for i in range(1, n+2):
        while stack and top[stack[-1]] > top[i]:
            pos = stack.pop()
            width = i - 1 - stack[-1]
            height = top[pos]
            area = max(area, width * height)

        stack.append(i)

    print(area)
