import sys

sys.stdin = open("input.txt", "r")
N, K  = list(map(int, sys.stdin.readline().split()))

n = list(sys.stdin.readline().rstrip())
print(n)

l = 0
stack = []

for i in range(len(n)):
    if not stack:
        stack.append(n[i])
    else:
        if l == K:
            stack.append(n[i])
        else:
            while True:
                if stack[-1] >= n[i]:
                    stack.append(n[i])
                    break

                else:
                    stack.pop()
                    l += 1 

                if l == K or not stack:
                    stack.append(n[i])
                    break

while l != K:
    stack.pop()
    l += 1
    
answer = ''

for s in stack:
    answer += s
print(answer)