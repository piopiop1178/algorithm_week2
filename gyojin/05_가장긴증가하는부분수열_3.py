import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0]

for i in range(n):
    low = 0
    high = len(dp) - 1
    while low <= high:
        mid = (low + high) // 2
        if dp[mid] < nums[i]:
            low = mid + 1
        else:
            high = mid - 1

    if low >= len(dp):
        dp.append(nums[i])
    else:
        dp[low] = nums[i]

print(len(dp) - 1)