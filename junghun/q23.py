import sys

# 10828 문제
from collections import deque

sys.stdin = open("input.txt", "r")

# Matrix 생성
N = int(sys.stdin.readline())

# 사과 갯수, 좌표 값 저장
apples = int(sys.stdin.readline())
apples_arr = list()
for _ in range(apples):
    row, column = map(int, sys.stdin.readline().split())
    apples_arr.append({"row": row, "column": column})

# 뱀의 움직임 수, 패턴 저장
turns = int(sys.stdin.readline())
turns_arr = list()
for _ in range(turns):
    second, direction = map(str, sys.stdin.readline().split())
    turns_arr.append({"second": int(second), "direction": direction})

# 게임 시작
second_cnt = 0
snake_arr = list()
snake_arr.append({"row": 1, "column": 1})
std_direction = "right"
# 게임 시작
while True:
    second_cnt += 1
    tmp = snake_arr[-1]
    prev_row = tmp['row']
    prev_column = tmp['column']

    if std_direction == "right":
        current_location = {"row": prev_row, "column": prev_column + 1}
    elif std_direction == "left":
        current_location = {"row": prev_row, "column": prev_column - 1}
    elif std_direction == "up":
        current_location = {"row": prev_row - 1, "column": prev_column}
    elif std_direction == "down":
        current_location = {"row": prev_row + 1, "column": prev_column}

    current_r = current_location["row"]
    current_c = current_location["column"]

    # 종료 조건 (1. 몸이 닿았을 때, 2 벽과 부딪혔을 때)
    if current_location in snake_arr:
        print(second_cnt)
        break

    elif current_c > N or current_r > N:
        print(second_cnt)
        break

    else:
        if apples_arr:
            if current_r == apples_arr[0]['row'] and current_c == apples_arr[0]['column']:
                snake_arr.append(current_location)
                del apples_arr[0]
            else:
                del snake_arr[0]
                snake_arr.append(current_location)

        if turns_arr:
            if turns_arr[0]['second'] == second_cnt:
                if turns_arr[0]['direction'] == "D":
                    if std_direction == "right":
                        std_direction = "down"
                    elif std_direction == "left":
                        std_direction = "up"
                    elif std_direction == "up":
                        std_direction = "right"
                    elif std_direction == "down":
                        std_direction = "left"

                elif turns_arr[0]['direction'] == "L":
                    if std_direction == "right":
                        std_direction = "up"
                    elif std_direction == "left":
                        std_direction = "down"
                    elif std_direction == "up":
                        std_direction = "left"
                    elif std_direction == "down":
                        std_direction = "right"

                del turns_arr[0]
