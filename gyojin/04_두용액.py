import sys

n = int(sys.stdin.readline())
liquid = sorted(list(map(int, sys.stdin.readline().split())))


limit = liquid[0] + liquid[-1]
small = 0
large = n-1

for i in range(1, n):
    pl = i
    pr = n - 1
    while pl <= pr:
        pc = (pl + pr) // 2
        mix = liquid[pl] + liquid[pc]

        if abs(mix) < abs(limit):
            limit = mix
            small = liquid[pl]
            large = liquid[pc]

        if mix == 0:
            print(liquid[small], liquid[large])
            sys.exit()
        elif mix > 0:
            pr = pc - 1
        else:
            pl = pc + 1

print(small, large)


