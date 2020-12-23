import sys

# 2504 문제
sys.stdin = open("input.txt", "r")


class FixedStack:
    def __init__(self, capacity):
        self.stk = [0] * capacity
        self.ptr = 0
        self.capacity = capacity

    def push(self, param):
        self.stk[self.ptr] = param
        self.ptr += 1

    def pop(self):
        self.ptr -= 1
        tmp = self.stk[self.ptr]
        self.stk[self.ptr] = 0
        return tmp

    def size(self):
        return self.ptr

    def clear(self):
        self.ptr = 0

    def peek(self):
        return self.stk[self.ptr - 1]


def check_form(param):
    stack = FixedStack(len(param))
    for i in range(len(param)):
        stack.push(param[i])
        if i > 0:
            cnt_push = stack.stk[stack.ptr - 1]
            pre_push = stack.stk[stack.ptr - 2]
            if pre_push == "(" and cnt_push == ")":
                stack.pop()
                stack.pop()
            if pre_push == "[" and cnt_push == "]":
                stack.pop()
                stack.pop()
    if stack.size() == 0:
        return True
    else:
        return False


def num_sum(n, stk):
    tmp_sum = 0
    while True:
        top = stk.pop()
        if top == '(' or top == "[":
            break
        tmp_sum += top
    return tmp_sum * n if tmp_sum else n


def cal(string):
    check = check_form(string)
    stack_cal = FixedStack(len(string))
    if check is False:
        return 0
    elif check is True:
        for str in string:
            if str == "(" or str == "[":
                stack_cal.push(str)
            elif str == ")":
                stack_cal.push(num_sum(2, stack_cal))
            elif str == "]":
                stack_cal.push(num_sum(3, stack_cal))

        return sum(stack_cal.stk)


case = input()
print(cal(case))
