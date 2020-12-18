import sys

sys.stdin = open("input.txt", "r")

N = int(input())
M = list(map(int, input().split()))
M.sort()

l = 0
r = len(M) - 1

ans = float('inf')
al, ar =  (0, 0)

if N == 2:
    al, ar = M[0], M[1]

else:
    while l < r:
        x = abs(M[l] + M[r])

        if x < ans:
            ans = x
            al, ar = M[l], M[r]
        
        if M[l] + M[r] >= 0:
            r -= 1
        else:
            l += 1
        
        # if abs(M[l] + M[r - 1]) >= abs(M[l + 1] + M[r]):
        #     l += 1
        # else:
        #     r -= 1

print(al, ar)