import sys
import heapq

n = int(sys.stdin.readline())
people = []
for _ in range(n):
    x = sorted(list(map(int, sys.stdin.readline().split())))
    people.append(x)
d = int(sys.stdin.readline())

people.sort()
print(people)

heap = []
for p in people:
    if p[1] - p[0] > d:
        continue
    else:
