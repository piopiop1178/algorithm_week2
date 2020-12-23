import copy
import sys

# 2812 문제
sys.stdin = open("input.txt", "r")


class FixedStack():
    def __init__(self, capa):
        self.stk = [None] * capa
        self.ptr = 0
        self.capacity = capa

    def push(self, param):
        self.stk[self.ptr] = param
        self.ptr += 1

    def pop(self):
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        if self.is_empty():
            return -1

        return self.stk[self.ptr - 1]

    def __len__(self):
        return self.ptr

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def is_empty(self) -> bool:
        return self.ptr <= 0


N, K = map(int, input().split())
copy_k = copy.deepcopy(K)
number_arr = input()
len_number = len(number_arr)
stack = FixedStack(N - K)

for idx, num in enumerate(number_arr):
    tmp_num = int(num)

    if len(stack) == 0:
        stack.push(tmp_num)

    else:
        while True:
            if not stack.is_empty() and K > 0:
                if stack.peek() < tmp_num:
                    stack.pop()
                    K -= 1
                else:
                    if stack.is_full():
                        break
                    else:
                        stack.push(tmp_num)
                        break
            else:
                if not stack.is_full():
                    stack.push(tmp_num)
                    break


for i in range(len(stack)):
    print(stack.stk[i], end="")
