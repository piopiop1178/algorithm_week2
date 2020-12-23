import sys

# 2164 문제 (카드2)
sys.stdin = open("input.txt", "r")

class FixedQueue:
    def __init__(self, param):
        self.front = 0
        self.rear = 0
        self.no = 0
        self.que = [None] * param
        self.capacity = param

    def enque(self, value):
        self.que[self.rear] = value
        self.no += 1
        self.rear += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self):
        tmp_value = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return tmp_value

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def is_empty(self) -> bool:
        return self.no <= 0


case = int(input())

que_test = FixedQueue(case)

for i in range(case):
    que_test.enque(i+1)

for i in range(que_test.no):
    if que_test.no > 1:
        que_test.deque()
        tmp = que_test.deque()
        que_test.enque(tmp)
    elif que_test.no == 1:
        break

print(que_test.que[que_test.front])
