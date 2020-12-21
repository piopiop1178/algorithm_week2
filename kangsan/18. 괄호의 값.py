import sys
s = sys.stdin.readline().rstrip()

def solution(s):
    stack = []
    n1, n2 = 0, 0
    num = 1
    answer = 0
    for i in range(len(s)):
        if s[i] == "[":
            n1 += 1
            num *= 3
            stack.append(s[i])

        elif s[i] == "(":
            n2 += 1
            num *= 2
            stack.append(s[i])

        elif s[i] == "]":
            n1 -= 1
            if n1 < 0:
                return 0

            if stack[-1] == "[":
                if s[i - 1] == "[":
                    answer += num
                num //= 3
                stack.pop()
        else:
            n2 -= 1
            if n2 < 0:
                return 0
            
            if stack[-1] == "(":
                if s[i - 1] == "(":
                    answer += num 
                num //= 2
                stack.pop()
                
    if n1 > 0 or n2 > 0:
        return 0 

    return answer

print(solution(s))

