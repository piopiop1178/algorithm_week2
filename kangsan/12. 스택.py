import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    c = sys.stdin.readline().split()

    if c[0] == "push":
        stack.append(int(c[1]))
    elif c[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif c[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif c[0] == "size":
        print(len(stack))
    else:
        if stack:
            print(stack.pop())
        else:
            print(-1)