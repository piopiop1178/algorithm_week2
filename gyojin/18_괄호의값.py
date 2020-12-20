import sys
test = sys.stdin.readline().rstrip()
n = len(test) - 1
tmp = []
ans = 1
result = 0

for i in range(n):
    if test[n] == '(' or test[n] == '[':
        print(0)
        break
    else:
        check = 0
        if test[i] == '(':
            ans *= 2
            tmp.append('(')
        elif test[i] == '[':
            ans *= 3
            tmp.append('[')
        else:
            try:
                tmp.pop()
                check = 1
            except IndexError:
                check = 1
                break

        if len(tmp) == 0 and check == 0:
            result += ans
            ans = 1
        elif len(tmp) == 0 and check == 1:
            result = 0
            break
        elif tmp[-1] == '(' and check == 1:
            result += ans
            ans = ans // 2
        elif tmp[-1] == '[' and check == 1:
            result += ans
            ans = ans // 3


print(result)



