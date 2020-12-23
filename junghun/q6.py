import sys

# 8983 문제 (사냥꾼)
from bisect import bisect_left, bisect_right

sys.stdin = open("input.txt", "r")

# 변수 저장
shot_point, num_animals, shot_length = map(int, input().split())
shot_point_arr = list(map(int, input().split()))
shot_point_arr.sort()
animals_arr = list()

for _ in range(num_animals):
    x, y = map(int, input().split())
    animals_arr.append((x, y))

# 사로를 기준으로 계산 할 것

cnt = 0
for animal in animals_arr:
    animal_x = animal[0]
    animal_y = animal[1]

    if animal_x > shot_point_arr[-1]:
        found_shot = len(shot_point_arr) - 1
    else:
        found_shot = bisect_left(shot_point_arr, animal_x, 0, len(shot_point_arr))
        if animal_x == found_shot or found_shot == 0:
            pass
        else:
            tmp_distance1 = abs(shot_point_arr[found_shot] - animal_x)
            tmp_distance2 = abs(shot_point_arr[found_shot - 1] - animal_x)
            if tmp_distance1 > tmp_distance2:
                found_shot -= 1

    distance = abs(shot_point_arr[found_shot] - animal_x) + animal_y
    if distance <= shot_length:
        cnt += 1

print(cnt)
