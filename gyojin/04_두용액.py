import sys

n = int(sys.stdin.readline())
liquid = sorted(list(map(int, sys.stdin.readline().split())))

pl = 0
pr = len(liquid) - 1
limit = liquid[pr] + liquid[0]
small = 0
large = 0

while pl < pr:
    # pc = (pl + pr) // 2
    mix = liquid[pl] + liquid[pr]

    if abs(mix) <= abs(limit):
        limit = mix
        small = pl
        large = pr
        if limit == 0:
            break

    if mix >= 0:
        pr -= 1
        # print('pl:', pl, 'pr:', pr)
    else:
        pl += 1
        # print('pl:', pl, 'pr:', pr)

print(liquid[small], liquid[large])



