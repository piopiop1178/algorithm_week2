import sys

# 2805 문제
sys.stdin = open("input.txt", "r")

tree_nums, target_len = map(int, input().split())
trees_len_arr = list(map(int, input().split()))
trees_len_arr.sort()
cut_len_list = list()


def binarySearch(key, arr):
    pl = 0
    pr = arr[-1]

    while True:
        if pl > pr:
            return "None"

        cutter_len = (pl + pr) // 2

        heights_sum = 0

        for tree in trees_len_arr:
            if tree > cutter_len:
                heights_sum = heights_sum + (tree - cutter_len)

        if heights_sum == key:
            return cutter_len

        elif heights_sum > key:
            cut_len_list.append([heights_sum, cutter_len])
            pl = cutter_len + 1

        elif heights_sum < key:
            pr = cutter_len - 1


found_len = binarySearch(target_len, trees_len_arr)

if found_len == "None":
    print(cut_len_list[-1][1])
else:
    print(found_len)