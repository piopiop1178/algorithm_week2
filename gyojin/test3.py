import sys
import heapq
from itertools import product


def multiply(arr):
    ans = 1
    for n in arr:
        if n == 0:
            return 0
        ans *= n
    return ans


K, N = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
inf = 100001

stack = []
heap = []


for i in range(1, inf):
    tmp = list(product(nums, repeat=i))
    for s in tmp:
        heapq.heappush(heap, multiply(s))
    while heap:
        k = heapq.heappop(heap)
        if k not in stack:
            stack.append(k)
        if len(stack) >= N:
            print(stack[-1])
            sys.exit()



# print(heap[0][1])
