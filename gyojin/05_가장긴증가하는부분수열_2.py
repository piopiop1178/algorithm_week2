import sys

n = int(sys.stdin.readline())
nums = sorted(map(int, sys.stdin.readline().split()))
ans = [0]


def binary_search(target: int):
    low = 0
    high = len(ans) - 1
    while low < high:
        mid = (low + high) // 2
        if ans[mid] < target:
            low = mid + 1
        elif ans[mid] > target:
            high = mid - 1
        else:
            low = high = mid
    return high


for num in nums:
    if ans[-1] < num:
        ans.append(num)
    else:
        ans[binary_search(num)] = num

print(len(ans) - 1)