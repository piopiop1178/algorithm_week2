# push
a = []
a.append(3)
a.append(5)
a.append(0)
print(a)        # [3, 5, 0]

# pop
top = a.pop()
print(top)      # 0
print(a)        # [3, 5]


from typing import Any
import sys


class FixedStack:
    ### 고정 길이 스택 클래스 ###

    class Empty(Exception):
        # 비어있는 스택에 pop 또는 peek할 때 내보내는 예외처리
        pass

    class Full(Exception):
        # 가득 찬 스택에 push할 때 내보내는 예외처리
        pass

    def __init__(self, capacity: int = 256) -> None:
        # 스택 초기화
        self.stk = [None] * capacity    # 스택 본체
        self.capacity = capacity        # 스택 크기
        self.ptr = 0                    # 스택 포인터

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
        # 스택에 value를 push(넣음)
        if self.is_full():              # 스택이 가득 찬 경우
            raise FixedStack.Full       # 예외 처리 발생
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        # 스택에서 꼭대기 데이터를 pop(꺼냄)
        if self.is_empty():             # 스택이 빈 경우
            raise FixedStack.Empty      # 예외 처리 발생
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        # 스택에서 꼭대기 데이터를 peek(들여다봄)
        if self.is_empty():             # 스택이 빈 경우
            raise FixedStack.Empty      # 예외 처리 발생
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> Any:
        # 스택에서 value를 찾아 인덱스 반환
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> int:
        # 스택에 있는 value 개수를 반환
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        # 스택에 value가 있는지 판단
        return self.count(value) >= 0

    def dump(self) -> None:
        # 스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])


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

