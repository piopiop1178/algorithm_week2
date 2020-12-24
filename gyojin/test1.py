import sys
N = int(sys.stdin.readline())
video = []
for _ in range(N):
    video.append(list(map(int, sys.stdin.readline().rstrip())))


def zip_image(x: int, y: int, n: int):

    summary = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            summary += video[i][j]

    if summary == 0:
        print('0', end='')
    elif summary == n**2:
        print('1', end='')

    else:
        print('(', end='')
        quad = n // 2
        zip_image(x, y, n - quad)
        zip_image(x, y + quad, n - quad)
        zip_image(x + quad, y, n - quad)
        zip_image(x + quad, y + quad, n - quad)
        print(')', end='')


zip_image(0, 0, N)
