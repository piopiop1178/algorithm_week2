import sys

a = int(sys.stdin.readline())
paper = list(list(map(int, sys.stdin.readline().split())) for _ in range(a))

cntW = 0
cntB = 0


def cut_paper(x: int, y: int, n: int):
    global cntW, cntB
    summary = 0

    for i in range(x, x + n):
        for j in range(y, y + n):
            summary += paper[i][j]

    if summary == 0:
        cntW += 1
    elif summary == n**2:
        cntB += 1
    else:
        quad = n // 2
        cut_paper(x, y, n - quad)
        cut_paper(x + quad, y, n - quad)
        cut_paper(x, y + quad, n - quad)
        cut_paper(x + quad, y + quad, n - quad)


cut_paper(0, 0, a)
print(cntW)
print(cntB)
