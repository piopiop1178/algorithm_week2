import sys

N, C = list(map(int, sys.stdin.readline()))
house = list(map(int, sys.stdin.readline()))
house.sort()

start = house[0] 
end = house[-1]

l = 0
r = house[-1]

answer = 1

while l <= r:
    m = (l + r) // 2

    if 1 + (m * (C - 1)) > end: 
        r = m - 1
    else:
        cnt = 1
        z = start + m

        for h in house:
            if h >= z:
                cnt += 1
                z = h + m

        if cnt >= C:
            answer = m
            l = m + 1
        else:
            r = m - 1
    
print(answer)