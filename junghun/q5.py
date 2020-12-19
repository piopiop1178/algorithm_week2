import sys

# 11053 문제
sys.stdin = open("input.txt", "r")

case = int(input())
sequence_arr = list(map(int, input().split()))

result_arr = [1] * case
tmp_set = set()

for i in range(case):
    tmp_set.clear()
    if i != 0:
        for j in range(i):
            std_value = sequence_arr[i]
            compare_value = sequence_arr[j]
            if compare_value < std_value:
                result_arr[i] = max(result_arr[i], result_arr[j] + 1)

print(max(result_arr))
