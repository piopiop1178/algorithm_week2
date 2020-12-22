import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
que = deque(i for i in range(1, n+1))
li = []
step = -(k-1)

while len(que) > 0:
    que.rotate(step)
    li.append(que.popleft())


result = ', '.join(str(li[i]) for i in range(n))
print('<' + result + '>')
