import sys

# 2493 문제 (탑)

class FixedStack():
    def __init__(self, capa):
        self.stk = [None] * capa
        self.capacity = capa
        self.ptr = 0

    def push(self, param):
        self.stk[self.ptr] = param
        self.ptr += 1

    def pop(self):
        self.ptr -= 1
        return self.stk[self.ptr]

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def __len__(self) -> int:
        # 스택에 쌓여 있는 데이터 개수 반환
        return self.ptr

    def peek(self):
        return self.stk[self.ptr-1]

sys.stdin = open("input.txt", "r")
case = int(sys.stdin.readline())
tower_arr = list(map(int, sys.stdin.readline().split()))
stack = FixedStack(case)
result_arr = list()

for idx, tower in enumerate(tower_arr):
    size_stack = len(stack)
    if size_stack == 0:
        stack.push((tower, idx + 1))
        result_arr.append(0)
    else:
        while len(stack) > 0 and stack.peek()[0] < tower:
            stack.pop()

        if len(stack) > 0:
            result_arr.append(stack.peek()[1])
        else:
            result_arr.append(0)

        stack.push((tower, idx + 1))

for i in range(len(result_arr)):
    if i == len(result_arr) - 1:
        print(result_arr[i])
    else:
        print(result_arr[i], end= " ")
