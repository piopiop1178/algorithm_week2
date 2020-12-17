import sys
# 1920번 문제
sys.stdin = open("input.txt", "r")

case = int(input())
given_nums_arr = list(map(int, input().split()))
given_nums_arr.sort()

case_search = int(input())
search_nums_arr = list(map(int, input().split()))


def binarySearch(key, num_arr):
    # 포인터 생성
    pl = 0
    pr = len(num_arr) - 1

    while True:
        pc = (pl + pr) // 2

        if pl > pr:
            return 0
        else:
            if num_arr[pc] == key:
                return 1
            elif num_arr[pc] > key:
                pr = pc - 1
            elif num_arr[pc] < key:
                pl = pc + 1


for num in search_nums_arr:
    print(binarySearch(num, given_nums_arr))
