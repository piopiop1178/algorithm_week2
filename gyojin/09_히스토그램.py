import sys

n1, test1 = int(sys.stdin.readline()), sorted(list(map(int, sys.stdin.readline().split())))
n2, test2 = int(sys.stdin.readline()), sorted(list(map(int, sys.stdin.readline().split())))
n3, test3 = int(sys.stdin.readline()), sorted(list(map(int, sys.stdin.readline().split())))


def histogram(n: int, hist: list):
    l = len(hist)
    for h in hist:
        tmp = []
        for i in range(l):
            if hist[i] - l >= 0:
                tmp[i] = hist[i] - l