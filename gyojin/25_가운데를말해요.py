import sys
import heapq


# def heap_sort(a: list):
#     heap = []
#     for i in a:
#         heapq.heappush(heap, i)
#     for j in range(len(a)):
#         a[j] = heapq.heappop(heap)
#     return a


n = int(sys.stdin.readline())
left = []
right = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, (-x, x))
    else:
        heapq.heappush(right, (x, x))

    if right and left[0][1] > right[0][1]:
        left_tmp = heapq.heappop(left)[1]
        right_tmp = heapq.heappop(right)[1]
        heapq.heappush(left, (-right_tmp, right_tmp))
        heapq.heappush(right, (left_tmp, left_tmp))

    print(left[0][1])

