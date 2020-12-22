import sys
N, B = map(int, sys.stdin.readline().split())
li = []
for _ in range(N):
    li.append(list(map(int, sys.stdin.readline().split())))


def matrix_product(a: list, b: list):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    return result


def matrix_pow(matrix: list, p: int):
    if p == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] = matrix[i][j] % 1000
        return matrix
    else:
        tmp = matrix_pow(matrix, p // 2)
        if p % 2 == 0:
            return matrix_product(tmp, tmp)
        else:
            return matrix_product(matrix_product(tmp, tmp), li)


ans = matrix_pow(li, B)
for row in ans:
    print(*row)
