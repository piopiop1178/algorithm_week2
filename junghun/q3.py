import sys

# 2110 문제
sys.stdin = open("input.txt", "r")

house_amount, router_amount = map(int, input().split())
house_arr = []
available_arr = []
# 이미 첫번째 인덱스에 공유기를 배치하기 때문에, 1을 제거한다
router_amount = router_amount - 1

for _ in range(house_amount):
    house_arr.append(int(input()))

house_arr.sort()


# d = distance , h = house
def binary_search(router, h_arr):
    end_h = h_arr[-1]
    d_pl = 1
    d_pr = end_h - 1

    while d_pl <= d_pr:
        std_d = (d_pl + d_pr) // 2
        start_h = h_arr[0]
        counter = 0
        isFlag = False

        if 1 + (std_d * router_amount) > end_h:
            d_pr = std_d - 1

        else:
            while True:
                next_h = start_h + std_d

                if next_h > end_h:
                    break

                if next_h in h_arr:
                    counter += 1
                    start_h = next_h
                    isFlag = True
                else:
                    h_pl = 0
                    h_pr = len(h_arr) - 1

                    while True:
                        h_pc = (h_pl + h_pr) // 2
                        h_mid = h_arr[h_pc]

                        if h_mid == next_h or h_pl > h_pr:
                            counter += 1
                            start_h = h_mid
                            break
                        elif h_mid > next_h:
                            h_pr = h_pc - 1
                        elif h_mid < next_h:
                            h_pl = h_pc + 1

            if counter >= router:
                available_arr.append([std_d, isFlag])
                d_pl = std_d + 1
            elif counter < router:
                d_pr = std_d - 1


binary_search(router_amount, house_arr)

print(available_arr)

# print(available_arr[-1][0])
