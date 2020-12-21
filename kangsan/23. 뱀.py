import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apples = set([])

for _ in range(K):
    x, y = list(map(int, sys.stdin.readline().split()))
    apples.add((y, x))

L = int(sys.stdin.readline())
times = []
for _ in range(L):
    info = sys.stdin.readline().split()
    info[0] = int(info[0])
    times.append(info)

snake = deque([])
body_set = set([])
direction = 90
now = (1, 1)
time = 0
cnt = 0
snake.append(now)
body_set.add(now)

while True:
    time += 1
    if direction == 90:
        now = (now[0] + 1, now[1])
    elif direction == 270:
        now = (now[0] - 1, now[1])
    elif direction == 0:
        now = (now[0], now[1] - 1)
    elif direction == 180:
        now = (now[0], now[1] + 1)
    
    if now[0] < 1 or now[1] < 1 or now[0] > N or now[1] > N:
        break
    if now in body_set:
        break
        
    snake.appendleft(now)
    body_set.add(now)
    
    if (now[0], now[1]) not in apples:
        body_set.remove(snake.pop())
    else:
        apples.remove((now[0], now[1]))

    if cnt < len(times) and times[cnt][0] == time:
        if times[cnt][1] == "L":
            direction -= 90
        else:
            direction += 90
        cnt += 1

    if direction < 0:
        direction += 360
    elif direction >= 360:
        direction -= 360    
    
print(time)