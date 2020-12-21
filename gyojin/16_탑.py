import sys
n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
tmp = []
laser = []

for i in range(n):
    while tmp:
        if tower[i] < tmp[-1][1]:            # 수신 가능
            laser.append(tmp[-1][0] + 1)
            break
        else:
            tmp.pop()
    if not tmp:
        laser.append(0)
    tmp.append([i, tower[i]])

for i in range(n):
    print(laser[i], end=' ')
