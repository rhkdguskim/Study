# https://school.programmers.co.kr/learn/courses/30/lessons/148652

# 1 : 1ea  [0, 1]
# 11011 : 5ea, [1, 4]
# 1101111011000001101111011 : 25ea [9, 16]
# ...                       : 25 * 5 ea, []

# 5로 나누었을때 몫이 3의 배수라면(?) -> r은 0이다.
# 5로 나누었을때 몫이 3의 배수가 아니라면(?) -> 나머지가 3이면 0

# 0, 1의 개수
import math

CASE_ZERO = [5, 0]
CASE_ONE = [1, 4]


def solution(n, l, r):
    def dfs(n, zero, one, end):
        if(n == end):
            return one
        
        new_v = [0, 0]
        new_v[0] += zero * 5
        new_v[0] += one
        new_v[1] += one * 4
        return dfs(n+1, new_v[0], new_v[1], end)

    
    s_1 = math.ceil(math.log(l, 5))
    s_2 = math.ceil(math.log(r, 5))
    
    d_1 = l % 5
    d_2 = r % 5
    
    
    temp1 = dfs(0, 0, 1, s_1)
    temp2 = dfs(0, 0, 1, s_2)
    
    print(temp1, temp2)
    if d_1:
        if s_1 % 3 != 0:
            if d_1 >= 3:
                d_1 -= 1
            
            temp1 += d_1
            
    
    if d_2:
        if s_2 % 3 != 0:
            if d_2 >= 3:
                d_2 -= 1
            
            temp2 += d_2
    
    answer = temp2 - temp1
    return answer

print(solution(2, 4, 17))