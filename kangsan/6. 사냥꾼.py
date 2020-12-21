import sys
sys.stdin = open("input.txt", "r")

M, N, L = list(map(int, sys.stdin.readline().split()))
sa = list(map(int, sys.stdin.readline().split()))
sa.sort()

answer = 0
for _ in range(N):
    l = 0
    r = M - 1
    x, y = list(map(int, sys.stdin.readline().split()))

    if y > L:
        continue

    while l <= r:
        c = (l + r) // 2
        
        if L - abs(sa[c] - x) >= y:
            answer += 1
            break
        else:
            if sa[c] - x < 0:
                l = c + 1
            else:
                r = c - 1

print(answer)