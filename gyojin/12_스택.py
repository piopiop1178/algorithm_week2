from typing import Any
import sys

class FixedStack:
    class Empty(Exception):
        # 비어있는 스택에 pop 또는 peek할 때 내보내는 예외처리
        pass

    class Full(Exception):
        # 가득 찬 스택에 push할 때 내보내는 예외처리
        pass

    def __init__(self, capacity: int = 10000) -> None:
        # 스택 초기화
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        # 스택에 쌓인 데이터 개수 반환
        return self.ptr

    def is_empty(self) -> bool:
        # 스택이 비어 있는지 판단
        return self.ptr <= 0

    def is_full(self) -> bool:
        # 스택이 가득 차있는지 판단
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            return -1
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            return -1
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0


n = int(sys.stdin.readline())
s = FixedStack(n)

for _ in range(n):
    order = sys.stdin.readline().split()
    command = order[0]

    if command == 'push':
        s.push(int(order[1]))
    elif command == 'pop':
        print(s.pop())
    elif command == 'size':
        print(len(s))
    elif command == 'empty':
        print(int(s.is_empty()))
    else:
        print(s.peek())

