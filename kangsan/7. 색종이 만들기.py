import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white = 0
blue = 0

def cut_paper(x, y, r):
    global blue, white
    color = paper[y][x]
    if r == 1:
        if color:
            blue += 1
        else:
            white += 1
        return 1

    for i in range(y, y + r):
        for j in range(x, x + r):
            if paper[i][j] != color:
                return cut_paper(x, y, r // 2) + cut_paper(x + r // 2, y, r // 2) + cut_paper(x, y + r // 2, r // 2) + cut_paper(x + r // 2, y + r // 2, r // 2)
    
    if color:
        blue += 1
    else:
        white += 1
    return 1

cut_paper(0, 0, N)

print(white, blue)