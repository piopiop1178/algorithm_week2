import sys

N = sys.stdin.readline().rstrip()

stack = ['(']
cnt = 0
for i in range(1, len(N)):
    if N[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if N[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
