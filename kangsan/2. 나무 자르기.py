#나무 리스트를 기준으로 이분탐색으로 하면 더 짧음 
#어떻게 통과?? 

N, M = 4, 7
tree = [20, 15, 10, 17, 16, 10, 16, 16, 16, 100, 80, 70, 99, 99, 95]
tree.sort(reverse=True)
n = 500000000
l = 0
r = 1000000000

c = 0
while True:
    s = 0
    for i in range(len(tree)):
        if tree[i] < n:
            break
        s += tree[i] - n
        if s > M:
            break

    if s > M:
        l = n
        c = (n + r) // 2
    elif s < M:
        r = n
        c = (n + l) // 2
    else:
        break

    if c == n:
        break
    else:
        n = c
    

print(n)
