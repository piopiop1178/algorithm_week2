import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

num = int(input())
matrix = []
blue = 0
white = 0
ans = []
for _ in range(num):
    line = list(map(int, input().rstrip()))
    matrix.append(line)

def cut(x, y, n):
    global blue, white
    check = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != matrix[i][j]:
                ans.append('(')
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                ans.append(')')
                return
    if check == 0:
        ans.append(0)
    else:
        ans.append(1)

cut(0,0,num)

print(*ans, sep='')