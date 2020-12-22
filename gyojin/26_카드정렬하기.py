import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    heapq.heappush(heap, x)

ans = 0
if len(heap) < 2:
    print(ans)
else:
    while len(heap) > 1:
        tmp = heapq.heappop(heap) + heapq.heappop(heap)
        ans += tmp
        heapq.heappush(heap, tmp)
    print(ans)
