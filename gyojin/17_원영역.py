import sys
N = int(sys.stdin.readline())
li = []
for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    li.append([x-r, -1, 0])    # 좌표, open, 상태
    li.append([x+r, 1, 0])     # 좌표, close, 상태

li.sort(key=lambda x: (x[0], -x[1]))
print(li)

stack = []
ans = 0
last = 0
for i in range(len(li)):

    if not stack:
        stack.append(li[i])
        last = li[i][0]

    else:
        if li[i][1] == -1:
            if li[i][0] == stack[-1][0]:     # 접할 때
                stack[-1][2] = '접함'
            else:
                if stack[-1][2] != '접함':
                    stack[-1][2] = '안접함'
                last = li[i][0]
            stack.append(li[i])
            # print('원열림:', stack)

        elif li[i][1] == 1:       # 원 닫힘
            tmp = stack.pop()
            if last == li[i][0]:
                ans += 1
            if stack and stack[-1][2] == '접함':
                last = li[i][0]

            ans += 1

    print('stack:', stack)
    print('ans:', ans)
    print('last:', last)


# print(stack)
print(ans + 1)

