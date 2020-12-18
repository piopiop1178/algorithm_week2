import sys

n = int(sys.stdin.readline())
nums = sorted(map(int, sys.stdin.readline().split()))
ans = [0]
# print(number)


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

# ans = 0
# tmp = 0
# for i in range(n):
#     cnt = 1
#     low = i
#     high = n - 1
#     while low <= high:
#         mid = (low + high) // 2
#         dif = nums[mid] - nums[i]
#
#         if dif > 0 and dif > tmp:
#             tmp = dif
#             low = mid + 1
#             cnt += 1
#         elif dif > 0:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     if ans < cnt:
#         ans = cnt
#
# print(ans)
