import sys

# 11279 문제 (최대 힙 문제)
sys.stdin = open("input.txt", "r")

case = int(sys.stdin.readline())


def swap(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def siftdown(a, i, size):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l <= size - 1 and a[l] > a[i]:
        largest = l
    if r <= size - 1 and a[r] > a[largest]:
        largest = r
    if largest != i:
        swap(a, i, largest)
        siftdown(a, largest, size)


def siftup(a, i):
    if i > 0:
        parent = (i - 1) // 2
        if a[i] > a[parent]:
            a[i], a[parent] = a[parent], a[i]
            siftup(a, parent)


def heapify(a, size):
    p = (size // 2) - 1
    while p >= 0:
        siftdown(a, p, size)
        p -= 1

    # phase 1
    size = len(a)
    heapify(a, size)


heap_arr = []

for _ in range(case):
    input_num = int(sys.stdin.readline())

    if input_num == 0:
        if len(heap_arr) == 0:
            print(0)
        else:
            print(heap_arr[0])
            heap_arr[0] = heap_arr[-1]
            heap_arr.pop()
            siftdown(heap_arr, 0, len(heap_arr))

    else:
        heap_arr.append(input_num)
        idx = len(heap_arr) - 1
        siftup(heap_arr, idx)
