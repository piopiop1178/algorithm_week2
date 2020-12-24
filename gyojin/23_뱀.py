import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apple = deque()
for _ in range(k):
    apple.append(list(map(int, sys.stdin.readline().split())))
l = int(sys.stdin.readline())
way = {}
for i in range(l):
    t, d = sys.stdin.readline().split()
    way[int(t)] = d

snake = deque([[1, 1]])
# 좌표 전환
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = 1, 1
direction = 0
time = 0
while True:
    x, y = x + dx[direction], y + dy[direction]
    time += 1
    if 0 < y < n+1 and 0 < x < n+1 and snake.count([x, y]) < 1:
        if apple.count([x, y]) < 1:
            snake.popleft()
        else:
            apple.remove([x, y])
        snake.append([x, y])

        if time in way.keys():
            if way[time] == 'L':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4

    else:
        print(time)
        break



