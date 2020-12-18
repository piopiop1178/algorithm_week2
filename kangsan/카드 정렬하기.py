import sys
import heapq

N = int(sys.stdin.readline())
heap = []

for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline()))

ans = 0
if len(heap) != 1:
    while heap:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        c = a + b
        ans += c

        if not heap:
            break
        heapq.heappush(heap, c)
    
print(ans)