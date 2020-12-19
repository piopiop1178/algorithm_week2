import sys

# 2470 문제
sys.stdin = open("input.txt", "r")

case = int(input())
ph_arr = list(map(int, input().split()))
ph_arr.sort()

pl = 0
pr = len(ph_arr) - 1
min_value = (0, 0, 0)

while pl < pr:
    left_value = ph_arr[pl]
    right_value = ph_arr[pr]
    sum_value = left_value + right_value

    if min_value[0] == 0 or sum_value == 0:
        min_value = (sum_value, left_value, right_value)
    elif abs(sum_value) < abs(min_value[0]):
        min_value = (sum_value, left_value, right_value)

    if sum_value == 0:
        break
    elif sum_value > 0:
        pr -= 1
    elif sum_value < 0:
        pl += 1

print(min_value[1], min_value[2])
