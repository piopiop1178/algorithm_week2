import sys

N, B = list(map(int, sys.stdin.readline().split()))
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def f(a, b):
    if b == 1:
        m = A
        for i in range(N):
            for j in range(N):
                m[i][j] = A[i][j] % 1000
        return m

    if b % 2 != 0:
        m = f(a, b - 1)
        nm = [[0 for _ in range(N)] for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    nm[i][j] = nm[i][j] + m[i][k] * a[k][j]

        for i in range(N):
            for j in range(N):
                nm[i][j] = nm[i][j] % 1000
                
        return nm

    else:
        m = f(a, b // 2)
        nm = [[0 for _ in range(N)] for _ in range(N)]

        for i in range(N):
            for j in range(N):
                m[i][j] = m[i][j] % 1000

        for i in range(N):
            for j in range(N):
                for k in range(N):
                    nm[i][j] = nm[i][j] + m[i][k] * m[k][j]

        for i in range(N):
            for j in range(N):
                nm[i][j] = nm[i][j] % 1000
        return nm

answer = f(A, B)

for i in range(N):
    print(*answer[i])           


