import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))

num_li = deque([str(i + 1) for i in range(N)])
answer = []

# cnt = 1
# while len(answer) < N:
#     if cnt != K:
#         cnt += 1
#         num_li.append(num_li.popleft())
#     else:
#         answer.append(num_li.popleft())
#         cnt = 1

# print('<' + ', '.join(answer) + '>')

num_li = [str(i + 1) for i in range(N)]
i = 0
while num_li:
    i = (i + K - 1) % len(num_li)
    answer.append(num_li.pop(i))
    
print('<' + ', '.join(answer) + '>')


