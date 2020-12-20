import sys
t = int(sys.stdin.readline())

for _ in range(t):
    test = sys.stdin.readline().rstrip()
    R = len(test) - 1
    if test[R] == '(':
        print('NO')
        continue
    else:
        tmp = []
        check = 0
        for j in range(len(test)):
            if test[j] == '(':
                tmp.append(test[j])
            else:
                try:
                    tmp.pop()
                except IndexError:
                    print('NO')
                    check = 1
                    break
        if len(tmp) != 0 and check == 0:
            print('NO')
        elif len(tmp) == 0 and check == 0:
            print('YES')
