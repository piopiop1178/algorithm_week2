import sys

N = int(input())
P = list(map(int, sys.stdin.readline().split()))

P.sort()
ans = [P[0], P[-1]]

min = P[0] + P[-1]
for i in range(len(P)):
    low = i + 1  # i+1부터 탐색 시작
    high = N - 1

    while low <= high:
        mid = (low + high) // 2
        tmp = P[i] + P[mid]

        if abs(tmp) < abs(min):
            min = tmp
            ans = [P[i], P[mid]]

        if tmp < 0:
            low = mid + 1
        elif tmp > 0:
            high = mid - 1
        elif tmp == 0:
            print(str(P[i]) + ' ' + str(P[mid]))
            exit(0)

print(str(ans[0]) + ' ' + str(ans[1]))
