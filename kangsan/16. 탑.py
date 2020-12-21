import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
tops = list(map(int, sys.stdin.readline().split()))

answer = [0] * N
stack = []

n = N - 1

while tops:
    if not stack:
        stack.append((n, tops.pop()))
    else:
        i, t = n, tops.pop()
        
        while stack:
            if stack[-1][1] > t:
                stack.append((n, t))
                break
            else:
                answer[stack[-1][0]] = n + 1
                stack.pop()

            if not stack:
                stack.append((n, t))
                break     
    n -= 1

print(*answer)
