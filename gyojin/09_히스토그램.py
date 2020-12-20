import sys

n1, test1 = int(sys.stdin.readline()), sorted(list(map(int, sys.stdin.readline().split())))
n2, test2 = int(sys.stdin.readline()), sorted(list(map(int, sys.stdin.readline().split())))
n3, test3 = int(sys.stdin.readline()), sorted(list(map(int, sys.stdin.readline().split())))


def histogram(n: int, hist: list):
    start = hist[0]
    last = len(hist) - 1
    min_height = hist.index(min(hist))
    area = (min_height - start) + (last - min_height)

    if min_height > start:
        histogram(hist[start:min_height])