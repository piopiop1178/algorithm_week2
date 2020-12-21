import sys

# 10773 문제
sys.stdin = open("input.txt", "r")


class FixedStack:

    def __init__(self, capacity) -> None:
        self.stk = [None] * capacity
        self.ptr = 0
        self.capacity = capacity

    def push(self, param: int):
        self.stk[self.ptr] = param
        self.ptr += 1

    def pop(self):
        self.ptr -= 1
        return self.stk[self.ptr]

    def size(self):
        return self.ptr - 1


case = int(input())
stack = FixedStack(case)

for _ in range(case):
    tmp = int(input())

    if tmp != 0:
        stack.push(tmp)
    elif tmp == 0:
        test = stack.pop()

len_stack = stack.ptr
tmp_sum = 0

for i in range(len_stack):
    item = stack.stk[i]
    tmp_sum = tmp_sum + item

print(tmp_sum)







