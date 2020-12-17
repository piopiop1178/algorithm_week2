import sys

n, c = map(int, sys.stdin.readline().split())
wifi = sorted(list(int(sys.stdin.readline()) for _ in range(n)))

print(wifi)
pl = min(wifi)
pr = max(wifi)


while True:
    width = []


