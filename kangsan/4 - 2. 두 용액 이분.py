import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
liquids = list(map(int, sys.stdin.readline().split()))
liquids.sort()

answer = float('inf')
al, ar = 0, 0

for i in range(N):
    l = i + 1
    r = N - 1
    while l <= r:
        m = (l + r) // 2
        tmp = liquids[i] + liquids[m]
        if abs(tmp) < answer:
            answer = abs(tmp)
            al, ar = liquids[i], liquids[m]
        
        if tmp >= 0:
            r = m - 1
        else:
            l = m + 1 

    if answer == 0:
        break

print(al, ar)