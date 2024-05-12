# https://school.programmers.co.kr/learn/courses/30/lessons/76502
from collections import deque

def solution(s):
    # 개수가 0이거나 홀수라면 만들수 없다.
    if len(s) == 0 or len(s) % 2 == 1:
        return 0
    
    def check(s):
        stack = []
        # (), [], {}
        check_v = {'}' : '{', ']' : '[', ')' :'('}
        cnt = 0
        for c in s:
            if c in check_v.values():
                stack.append(c)
            else:
                if not stack:
                    return False, cnt
                
                if stack[-1] != check_v[c]:
                    return False, cnt
                
                stack.pop()
                if not stack:
                    cnt += 1
        
        return len(stack) == 0, cnt
    
    s = deque(s)
    for _ in range(len(s)):
        c, cnt = check(s)
        #print(s, c, cnt)
        if c:
            return cnt
        s.rotate(-1)
        
    return 0