import sys
n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().rstrip()))
stack = []


while num and len(stack) <= k:
    top = num.pop()

    if len(stack) > 0:
        while stack and top >= stack[-1]:
            num.append(stack.pop())

        if len(stack) < k:
            stack.append(top)

    else:
        stack.append(top)


for i in stack:
    print(i, end='')
