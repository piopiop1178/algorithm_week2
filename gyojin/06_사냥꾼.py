import sys
m, n, l = map(int, sys.stdin.readline().split())
shooter = list(map(int, sys.stdin.readline().split()))
animal = []
cnt = 0

for _ in range(n):
    animal.append(list(map(int, sys.stdin.readline().split())))

shooter.sort()


for ani in animal:
    lower_bound = ani[0] + ani[1] - l
    upper_bound = ani[0] - ani[1] + l
    low = 0
    high = m - 1

    if ani[1] > l:
        continue

    while low <= high:
        mid = (low + high) // 2
        if shooter[mid] < lower_bound:
            low = mid + 1
        elif shooter[mid] > upper_bound:
            high = mid - 1
        else:
            cnt += 1
            break


print(cnt)
# print(len(ans))