import sys

# 9012 문제
sys.stdin = open("input.txt", "r")

case = int(input())


class FixedStack:
    def __init__(self, capacity: int(50)):
        self.stk = [None] * capacity
        self.ptr = 0
        self.capacity = capacity

    def push(self, param):
        self.stk[self.ptr] = param
        self.ptr += 1

    def pop(self):
        self.ptr -= 1
        return self.stk[self.ptr]

    def size(self):g
        return self.ptr


for _ in range(case):
    test_str = input()
    len_str = len(test_str)

    stack = FixedStack(len_str)
    for i in range(len_str):
        stack.push(test_str[i])
        if i > 0:
            cnt_push = stack.stk[stack.ptr - 1]
            pre_push = stack.stk[stack.ptr - 2]
            if pre_push == "(" and cnt_push == ")":
                stack.pop()
                stack.pop()

    if stack.size() == 0:
        print("YES")
    else:
        print("NO")

