import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    h = int(sys.stdin.readline())
    
    if stack:
        while stack:
            if stack[-1] <= h:
                stack.pop()

            if not stack:
                stack.append(h)
                break

            elif stack[-1] > h:
                stack.append(h)
                break
    else:
        stack.append(h)

print(stack)