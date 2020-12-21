import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
apple = deque()
for _ in range(k):
    apple.append(list(map(int, sys.stdin.readline().split())))
l = int(sys.stdin.readline())
way = deque()
for _ in range(l):
    way.append(list(map(str, sys.stdin.readline().split())))

snake = deque([[0, 0]])
# 좌표 전환
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = 1, 1
direction = 0
time = 0
while True:
    x, y = x + dx[direction], y + dy[direction]
    if 0 < y < n+1 and 0 < x < n+1 and snake.count([x, y]) < 1:
        if apple.count([x, y]) < 1:
            snake.popleft()
        snake.append([x, y])
        for i in range(l):
            if time == int(way[i][0]):
                if way[i][1] == 'L':
                    direction = (direction + 1) % 4
                else:
                    direction = (direction - 1) % 4
        time += 1

    else:
        print(time)
        break



