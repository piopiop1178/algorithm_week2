import sys
n = int(sys.stdin.readline())
stick = [int(sys.stdin.readline()) for _ in range(n)]
tmp = [stick[-1]]

for i in range(n-1, -1, -1):
    if stick[i] > tmp[-1]:
        tmp.append(stick[i])
        stick.pop()
    else:
        stick.pop()

print(len(tmp))
