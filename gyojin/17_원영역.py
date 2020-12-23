import sys

sys.stdin = open("input.txt", "r")
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
for i in range(len(li)):

    if not stack:
        stack.append([li[i], 'open'])
        last = li[i][0]

    else:
        if li[i][1] == -1:
            if li[i][0] == last:     # 접할 때
                stack[-1][1] = '접'
            else:
                if stack[-1][1] != '접':
                    stack[-1][1] = '안접'
                last = li[i][0]
            stack.append([li[i], 'open'])
            # print('원열림:', stack)

        elif li[i][1] == 1:       # 원 닫힘
            tmp = stack.pop()
            if stack and stack[-1][1] == '접':
                last = li[i][0]
                # last = li[i][0]
                # print('접:',ans)
            if tmp[0][0] == li[i][0]:
                ans += 1
            ans += 1
            # print('tmp:', tmp)
            # print('last:',last)
    print('stack:', stack)
    print('ans:', ans)
    print('last:', last)


# print(stack)
print(ans)

