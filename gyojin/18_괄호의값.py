import sys

test = sys.stdin.readline().rstrip()
n = len(test) - 1
stack = []

if test[n] == '(' or test[n] == '[':
    print(0)
    sys.exit()
else:
    for i in test:

        if i == ')':
            tmp = 0

            while stack:
                top = stack.pop()

                if top == '(':
                    if tmp == 0:
                        stack.append(2)
                    else:
                        stack.append(2 * tmp)
                    break

                elif top == '[':
                    print(0)
                    sys.exit()

                else:
                    if tmp == 0:
                        tmp = int(top)
                    else:
                        tmp = tmp + int(top)

        elif i == ']':
            tmp = 0

            while stack:
                top = stack.pop()

                if top == '[':
                    if tmp == 0:
                        stack.append(3)
                    else:
                        stack.append(3 * tmp)
                    break

                elif top == '(':
                    print(0)
                    sys.exit()

                else:
                    if tmp == 0:
                        tmp = int(top)
                    else:
                        tmp = tmp + int(top)
        else:
            stack.append(i)

try:
    print(sum(stack))
except:
    print(0)
