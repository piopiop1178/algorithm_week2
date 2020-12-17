import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

pl = 0
pr = max(trees)

while pl <= pr:
    bin = 0
    pc = (pl + pr) // 2
    for tree in trees:
        cut = tree - pc
        if cut > 0:
            bin += cut

    if bin >= m:
        ans = pc
        pl = pc + 1
    else:
        pr = pc - 1

print(ans)

# def bin_cut(a: list, key: int):
#     pl = 0
#     pr = max(a)
#
#     while True:
#         tmp.clear()
#         pc = (pl + pr) // 2
#         for tree in trees:
#             if tree - pc > 0:
#                 tmp.append(tree - pc)
#             else:
#                 tmp.append(0)
#
#         if sum(tmp) == key:
#             return pc
#
#         if sum(tmp) < key:
#             pr = pc - 1
#         else:
#             pl = pc + 1


# print(bin_cut(trees, m))
