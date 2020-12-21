import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

for b in B:
    l = 0
    r = len(A) - 1

    while True:
        center = (l + r) // 2
        
        if b == A[center]:
            print(1)
            break
        elif b < A[center]:
            r = center - 1
        else:
            l = center + 1
        
        if l > r:
            print(0)
            break

# import sys
# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))

# A_dic = {}

# for a in A:
#     A_dic[a] = A_dic.get(a, 0) + 1    

# M = int(sys.stdin.readline())
# B = list(map(int, sys.stdin.readline().split()))

# for b in B:
#     if A_dic.get(b):
#         print(1)
#     else:
#         print(0)