import sys

N = int(sys.stdin.readline())
points = []
for _ in range(N):
    x, r =list(map(int, sys.stdin.readline().split()))
    points.append(["{", x - r, 0, 0]) #괄호, 좌표, 상태(이어지면 1 아니면  0), 이어진 원 지름 길이의 합  
    points.append([")", x + r, 0, 0])
points.sort(key=lambda x:(x[1], x[0])) #같은 좌표일 때 닫는 괄호가 먼저 나와야해서 { 보다 값이 작은 ) 를 사용함 
stack = []
answer = 1

for i in range(len(points)):
    if points[i][0] == "{":
        if stack:
            if stack[-1][1] == points[i][1] or stack[-1][3] == points[i][1]: 
                stack[-1][2] = 1
            elif stack[-1][3] != points[i][1]:
                stack[-1][2] = 0
        stack.append(points[i])

    else:
        half = stack.pop()
        if stack and stack[-1][2] == 1:
            stack[-1][3] = points[i][1]
        
        if half[2] == 1 and half[3] == points[i][1]:
            answer += 1
        answer += 1
print(answer)

