import sys


def dist(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2


def devi(st, en):
    leng = en - st
    if leng == 2:
        return dist(point[st], point[st + 1])
    elif leng == 3:
        return min(dist(point[st], point[st + 1]), dist(point[st + 1], point[st + 2]),
                   dist(point[st], point[st + 2]))

    mid = (st + en) // 2
    d = min(devi(st, mid), devi(mid, en))  # 왼쪽 분할 / 오른쪽 분할 거리 최소값
    p = point[mid][0]
    tmp = []

    for i in range(st, en):
        if (p - point[i][0]) ** 2 <= d:
            tmp.append(point[i])
    tmp.sort(key=lambda x: x[1])

    mini = d
    tmp_len = len(tmp)
    if tmp_len >= 2:
        for i in range(tmp_len - 1):
            for j in range(i + 1, tmp_len):
                if (tmp[i][1] - tmp[j][1]) ** 2 > d:
                    break
                elif tmp[i][0] < mid and tmp[j][0] < mid:
                    continue  # 왼쪽 파티션 제외
                elif tmp[i][0] > mid and tmp[j][0] > mid:
                    continue  # 오른쪽 파티션 제외
                mini = min(mini, dist(tmp[i], tmp[j]))
    return mini


n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(list(map(int, sys.stdin.readline().split())))
point = list(set(map(tuple, li)))

if len(point) != len(li):
    print(0)
else:
    point.sort()
    print(devi(0, len(point)))
