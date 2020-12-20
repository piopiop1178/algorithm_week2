import sys

n, c = map(int, sys.stdin.readline().split())
house = sorted(list(int(sys.stdin.readline()) for _ in range(n)))

min_width = 1
max_width = house[-1] - house[0]
ans = 0


while min_width <= max_width:
    cnt = 1
    rout = house[0]
    width = (min_width + max_width) // 2

    for i in range(1, n):
        if house[i] >= rout + width:
            cnt += 1
            rout = house[i]

    if cnt >= c:
        ans = width
        min_width = width + 1
    else:
        max_width = width - 1

print(ans)

# pl = 0
# pr = len(wifi) - 1
# mini = 0
#
#
# while pl < pr:
#     pl = 0
#     cnt = c - 1
#     width = (pl + pr) // 2
#
#     for i in range(1, pr):
#         if wifi[i] - wifi[pl] >= width:
#             cnt -= 1
#             pl = i
#
#     if cnt > 0:
#         width = width - 1
#     else:
#         mini = width
#         width = width + 1
#
#
# print(mini)
