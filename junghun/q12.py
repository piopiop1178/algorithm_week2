from typing import Any
import sys

# 10828 문제
sys.stdin = open("input.txt", "r")


class FixedStack:
    class Empty(Exception):
        pass

    def __init__(self, capacity) -> None:
        # "스택 초기화"
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        # 스택에 쌓여 있는 데이터 개수 반환
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= stack_test.capacity

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Empty
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        if self.is_empty():
            return -1
        return self.stk[self.ptr - 1]


case = int(sys.stdin.readline())
cmd_arr = list()
stack_test = FixedStack(case)

for _ in range(case):
    cmd_arr.append(sys.stdin.readline().split())

for cmd in cmd_arr:
    cmd_act = cmd[0]
    if cmd_act == "push":
        cmd_val = cmd[1]
        stack_test.push(cmd_val)
    elif cmd_act == "top":
        print(stack_test.peek())
    elif cmd_act == "size":
        print(stack_test.ptr)
    elif cmd_act == "empty":
        print(int(stack_test.is_empty()))
    elif cmd_act == "pop":
        print(stack_test.pop())
