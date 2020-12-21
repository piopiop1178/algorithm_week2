import sys
n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().rstrip()))
stack = []


for i in range(n):

    while stack and stack[-1] < num[i] and k > 0:
        stack.pop()
        k -= 1
    stack.append(num[i])

while k > 0:
    stack.pop()
    k -= 1

for i in stack:
    print(i, end='')
