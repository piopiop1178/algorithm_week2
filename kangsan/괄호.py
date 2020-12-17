import sys

sys.stdin = open("input.txt", "r")
T = int(sys.stdin.readline())

for _ in range(T):
    ps = sys.stdin.readline().rstrip()

    s = 0
    for p in ps:
        if p == "(":
            s += 1
        else:
            s -= 1
        if s < 0:
            break 
        
    if s == 0:
        print('YES')
    else:
        print('NO')

