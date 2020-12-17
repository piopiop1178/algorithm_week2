import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
queue = deque([])

for _ in range(N):
    c = sys.stdin.readline().split()

    if c[0] == "push":
        queue.append(int(c[1]))
    elif c[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif c[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    elif c[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif c[0] == "size":
        print(len(queue))
    else:
        if queue:
            print(queue.popleft())
        else:
            print(-1)