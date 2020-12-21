import sys

# 17608 문제 (막대기)
sys.stdin = open("input.txt", "r")

case = int(sys.stdin.readline())


class FixedStack:
    def __init__(self, capa: int):
        self.stk = [None] * capa
        self.ptr = 0
        self.capacity = capa

    def push(self, param):
        self.stk[self.ptr] = param
        self.ptr += 1

    def pop(self):
        self.ptr -= 1
        return self.stk[self.ptr]

    def size(self):
        return self.ptr


stack = FixedStack(case)

for i in range(case):
    tmp_stick = int(sys.stdin.readline())

    if stack.size() == 0:
        stack.push(tmp_stick)

    elif stack.size() == 1:
        if stack.stk[stack.ptr - 1] <= tmp_stick:
            stack.pop()
        stack.push(tmp_stick)
    else:
        while stack.size() > 0:
            if stack.stk[stack.ptr - 1] <= tmp_stick:
                stack.pop()
            else:
                break
        stack.push(tmp_stick)


print(stack.size())

# 697646
