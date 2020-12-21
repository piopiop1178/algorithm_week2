import sys

k = int(sys.stdin.readline())
tmp = []
for _ in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        tmp.pop()
    else:
        tmp.append(num)

print(sum(tmp))
