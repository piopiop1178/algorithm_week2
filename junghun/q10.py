import sys

# 10830 문제 (행렬 제곱)
sys.stdin = open("input.txt", "r")


def productMatrix(mat1, mat2, n):
    matR = [len(mat2[0]) * [0] for i in range(len(mat1))]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matR[i][j] += mat1[i][k] * mat2[k][j]
            matR[i][j] %= 1000

    return matR


def multi(a, b, n):
    if b == 1:
        tmp_matrix = [n * [0] for i in range(n)]
        for i in range(n):
            for j in range(n):
                tmp_matrix[i][j] = a[i][j] % 1000
        return tmp_matrix
    else:
        tmp = multi(a, b // 2, n)
        if b % 2 == 0:
            return productMatrix(tmp, tmp, n)
        else:
            return productMatrix(productMatrix(tmp, tmp, n), a, n)


# 변수 저장
size, times = map(int, input().split())
matrix = list()
for _ in range(size):
    matrix.append(list(map(int, input().split())))

result = multi(matrix, times, size)

for row in result:
    print(*row)
