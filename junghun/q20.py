import sys

# 18258 문제
from typing import Any

sys.stdin = open("input.txt", "r")


class FixedQueue:
    def __init__(self, capa) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capa
        self.que = [None] * capa

    def __len__(self):
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, param: Any) -> None:
        self.que[self.rear] = param
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:

        if self.is_empty():
            tmp_value = -1
        else:
            tmp_value = self.que[self.front]
            self.front += 1
            self.no -= 1
            if self.front == self.capacity:
                self.front = 0
        return tmp_value



case = int(sys.stdin.readline())
que = FixedQueue(case)

for _ in range(case):
    tmp_cmd = sys.stdin.readline().split()

    if tmp_cmd[0] == "push":
        cmd_val = tmp_cmd[1]
        que.enque(cmd_val)
    elif tmp_cmd[0] == "front":
        if que.is_empty():
            print(-1)
        else:
            print(que.que[que.front])

    elif tmp_cmd[0] == "back":
        if que.is_empty():
            print(-1)
        else:
            print(que.que[que.rear-1])
    elif tmp_cmd[0] == "size":
        print(que.no)
    elif tmp_cmd[0] == "empty":
        print(int(que.is_empty()))
    elif tmp_cmd[0] == "pop":
        print(que.deque())
