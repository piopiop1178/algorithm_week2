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
        if li[i][1] == -1:      ### 원이 열릴 때 ###

            if li[i][0] == stack[-1][0]:     # 접할 때
                stack[-1][2] = '접함'

            else:                            # 접하지 않을 때
                if stack[-1][2] != '접함' or last != li[i][0]:    # 이전 원이 접하지 않았을 때
                    stack[-1][2] = '안접함'                       #1 열린 후 이전 원의 왼쪽 좌표와 다를 때
                                                                 #2 닫힌 후 이전 원의 오른쪽 좌표와 다를 때
                last = li[i][0]
            stack.append(li[i])

        elif li[i][1] == 1:     ### 원이 닫힐 때 ###

            tmp = stack.pop()
            if last == li[i][0] and tmp[2] == '접함':             # 원이 최종적으로 닫힐 때
                ans += 1
            if stack and stack[-1][2] == '접함':
                last = li[i][0]

            ans += 1

    print('stack:', stack)
    print('ans:', ans)
    print('last:', last)


# print(stack)
print(ans + 1)

