import sys
import heapq

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    x = sorted(list(map(int, sys.stdin.readline().split())))
    people.append(x)
d = int(sys.stdin.readline())

people.sort(key=lambda x: x[1])

heap = []
maxi = 0
for i in range(n):
    heapq.heappush(heap, people[i][0])
    while heap and heap[0] < people[i][1] - d:
        heapq.heappop(heap)
    maxi = max(maxi, len(heap))

print(maxi)
