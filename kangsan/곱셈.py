import sys
a, b, c = list(map(int, sys.stdin.readline().split()))

def solution(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b % 2 != 0:
        return solution(a, b - 1) * a
    else:
        m = solution(a, b // 2)
        m = m % c
        return m ** 2  % c
        
print(solution(a, b) % c)





