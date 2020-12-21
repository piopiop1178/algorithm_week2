import sys

def max_square(l, r):
    if l == r:
        return h[l]
    else:
        m = (l + r) // 2
        nl = m
        nr = m + 1
        nh = min(h[nl], h[nr])
        tmp = nh * 2

        cnt = 2
        while True:
            if (h[nl] == 0 or nl == l) and (h[nr] == 0 or nr == r): 
                break 
            elif h[nl] == 0 or nl == l:
                if h[nr + 1] < nh:
                    nh = h[nr + 1]
                nr += 1
            elif h[nr] == 0 or nr == r:
                if h[nl - 1] < nh:
                    nh = h[nl - 1]
                nl -= 1
            else:
                if h[nl - 1] > h[nr + 1]:
                    if h[nl - 1] < nh:
                        nh = h[nl - 1]
                    nl -= 1
                else:
                    if h[nr + 1] < nh:
                        nh = h[nr + 1]
                    nr += 1
            cnt += 1
            tmp = max(tmp, nh * cnt)
        return(max(max_square(l, m), max_square(m + 1, r), tmp))  

while True:
    h = list(map(int, sys.stdin.readline().split()))
    if h[0] == 0:
        break
    print(max_square(1, len(h) - 1))
  
    
    
