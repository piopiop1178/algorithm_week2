import sys


def find(target):
    l, h = 1, len(stack) - 1
    while l < h:
        m = (l + h) // 2
        if stack[m] < target:
            l = m + 1
        elif stack[m] > target:
            h = m
        else:
            l = h = m
    return h


l = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = [0]
for a in arr:
    if stack[-1] < a:
        stack.append(a)
    else:
        stack[find(a)] = a
print(len(stack) - 1)
