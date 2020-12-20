import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
ans = [nums[0]]


for i in range(1, n):
    if ans[-1] < nums[i]:
        ans.append(nums[i])
    else:
        target = nums[i]
        low = 0
        high = len(ans) - 1
        while low <= high:
            mid = (low + high) // 2
            dif = ans[mid] - target
            if dif >= 0:
                high = mid - 1
            else:
                low = mid + 1

        ans[low] = nums[i]

print(len(ans))

