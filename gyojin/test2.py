import sys

N = sys.stdin.readline().rstrip()

stack = ['(']
cnt = 0
for i in range(1, len(N) - 1):
    if N[i] == '(':
        stack.append('(')
    else:
        if N[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1

print(cnt + 1)
