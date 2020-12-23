import sys

# 1715 문제 (카드 정렬하기)
from collections import deque

sys.stdin = open("input.txt", "r")


def heapify(arr, size):
    parent_node = (size // 2) - 1
    while parent_node >= 0:
        siftdown(arr, parent_node, size)
        parent_node -= 1


def siftdown(arr, parent, size):
    left_node = 2 * parent + 1
    right_node = left_node + 1
    largest = parent
    if left_node <= size - 1 and arr[left_node] < arr[largest]:
        largest = left_node
    if right_node <= size - 1 and arr[right_node] < arr[largest]:
        largest = right_node

    if largest != parent:
        arr[parent], arr[largest] = arr[largest], arr[parent]
        siftdown(arr, largest, size)


def siftup(arr, final_node):
    if final_node < 0:
        parent = (final_node - 1) // 2
        if arr[parent] > arr[final_node]:
            arr[parent], arr[final_node] = arr[final_node], arr[parent]
            siftup(arr, parent)


def pop(arr):
    tmp = arr[0]
    # del arr[0]
    if len(arr) == 1:
        arr.pop()

    elif len(arr) >= 2:
        arr[0] = arr[-1]
        arr.pop()

    siftdown(arr, 0, len(arr))

    return tmp


case = int(input())
nums_arr = list()

for _ in range(case):
    nums_arr.append(int(input()))

nums_size = len(nums_arr)
heapify(nums_arr, nums_size)

result_sum = 0
while len(nums_arr) > 1:
    num1 = pop(nums_arr)
    num2 = pop(nums_arr)
    tmp_sum = num1 + num2
    result_sum = result_sum + tmp_sum
    nums_arr.append(tmp_sum)
    siftup(nums_arr, len(nums_arr) - 1)

print(result_sum)
