import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
I = [A[0]]

for i in range(1, len(A)):
    if I[-1] < A[i]:
        I.append(A[i])
    else:
        l = 0
        r = len(I) - 1
        while l <= r:
            m = (l + r) // 2
            if I[m] >= A[i]:
                r = m - 1
            else:
                l = m + 1
        I[l] = A[i]
        
print(len(I))  