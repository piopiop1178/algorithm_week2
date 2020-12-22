import sys
import heapq

N = int(sys.stdin.readline())

heap_1 = []
heap_2 = []

for _ in range(N):
    n = int(sys.stdin.readline())
    if len(heap_1) == len(heap_2):
        heapq.heappush(heap_1, (-n, n))
    else:
        heapq.heappush(heap_2, n)
    if heap_1 and heap_2:
        if heap_1[0][1] > heap_2[0]:
            a = heapq.heappop(heap_1)
            b = heapq.heappop(heap_2)
            heapq.heappush(heap_1, (-b, b))
            heapq.heappush(heap_2, a[1])
    print(heap_1[0][1]) 


           