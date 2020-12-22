import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque(i for i in range(1, n+1))

while len(que) > 1:
    que.popleft()
    que.rotate(-1)

print(que.pop())
