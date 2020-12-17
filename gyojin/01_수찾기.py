
n = int(input())
inp = list(map(int, input().split()))
m = int(input())
comp = list(map(int, input().split()))

inp = sorted(inp)

def findN(a: list, key: int) -> int:
    left = 0
    right = len(a) - 1

    while True:
        center = (left + right) // 2
        if a[center] == key:
            return 1
        elif a[center] > key:
            right = center - 1
        else:
            left = center + 1
        if left > right:
            break
    return 0


for i in range(m):
    print(findN(inp, comp[i]))
