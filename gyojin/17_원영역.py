import sys
N = int(sys.stdin.readline())
li = []
for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    li.append([x-r, -1])    # open
    li.append([x+r, 1])     # close

li.sort(key=lambda x: (x[0], -x[1]))
print(li)

stack = []
leng = len(li) - 1
ans = 0
for i in range(leng):

    if not stack:
        stack.append([li[i], 'open'])
        last = li[i][0]
        print('처음:', last)

    else:
        if li[i][1] == -1:
            if li[i][0] == last:     # 접할 때
                stack[-1][1] = '접'
            else:
                stack[-1][1] = '안접'
                last = li[i][0]
            stack.append([li[i], 'open'])
            print('원열림:', last)

        elif li[i][1] == 1:       # 원 닫힘
            tmp = stack.pop()
            if tmp[1] == '접' and last == li[i][0]:
                ans += 2
            else:
                ans += 1
            last = li[i][0]
            print('원닫힘:', last)

print(ans + 1)

