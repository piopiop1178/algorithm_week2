import math
import sys

# 2630 문제 (색종이 만들기)
sys.stdin = open("input.txt", "r")

case = int(sys.stdin.readline())
matrix = list()
result_blue = 0
result_white = 0

for _ in range(case):
    matrix.append(list(map(int, sys.stdin.readline().split())))


def divide_conquer(x, y, n):
    global result_blue, result_white
    tmp_counter = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if matrix[i][j]:
                tmp_counter += 1
    if not tmp_counter:
        result_white += 1
    elif tmp_counter == n * n:
        result_blue += 1
    else:
        divide_conquer(x, y, n // 2)
        divide_conquer(x + n // 2, y, n // 2)
        divide_conquer(x, y + n // 2, n // 2)
        divide_conquer(x + n // 2, y + n // 2, n // 2)
    return


divide_conquer(0, 0, case)
print(result_white)
print(result_blue)

#
# def divide_paper(start_c, final_c, matrix_param):
#     global result_blue, result_white
#     len_matrix = (final_c[0] - start_c[0]) + 1
#     half_len = (len_matrix - 1) // 2
#     check_matrix = 0
#     sum_max = int(math.pow(len_matrix, 2))
#
#     for i in range(start_c[0], final_c[1] + 1):
#         for j in range(start_c[1], final_c[1] + 1):
#             tmp = matrix_param[i][j]
#             check_matrix = check_matrix + tmp
#
#     if check_matrix == 0:
#         result_white = result_white + 1
#     elif check_matrix == sum_max:
#         result_blue = result_blue + 1
#
#     else:
#         # 1사분면
#         divide_paper((start_c[0], start_c[1]), (start_c[0] + half_len, start_c[1] + half_len), matrix_param)
#         # 2사분면
#         divide_paper((start_c[0], start_c[1] + (half_len + 1)), (start_c[1] + half_len, len_matrix - 1), matrix_param)
#         # 3사분면
#         divide_paper((start_c[0] + (half_len + 1), start_c[0]), (len_matrix - 1, start_c[1] + half_len), matrix_param)
#         # 4사분면
#         divide_paper((start_c[0] + (half_len + 1), start_c[1] + (half_len + 1)), (len_matrix - 1, len_matrix - 1),
#                      matrix_param)
#
#     return
#
#
# start_location = (0, 0)
# final_location = (case - 1, case - 1)
#
# divide_paper(start_location, final_location, matrix)
#
# print(result_blue, result_white)
