import sys

n = int(sys.stdin.readline())
nums = sorted(map(int, sys.stdin.readline().split()))

# print(number)


ans = 0
for i in range(n):
    cnt = 1
    low = i
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        dif = nums[mid] - nums[low]

        if dif > 0:
            low = mid + 1
            cnt += 1
        else:
            high = mid - 1

    if ans < cnt:
        ans = cnt

print(ans)
