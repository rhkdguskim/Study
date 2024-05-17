# https://school.programmers.co.kr/learn/courses/30/lessons/87391
# 거꾸로 탐색해본다.
# x,y 위치에서 다른위치로 갈 수 있는 경우의 수

# (0, 0)
# ㅗ -> <- -> <- ㅗ
def solution(n, m, x, y, queries):
    LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3
    
    def is_range(i, max_value):
        return 0 <= i < max_value
        
    
    def move(s, e, cnt, max_value):
        n_s = 0 if s == 0 and cnt > 0 else s + cnt
        n_e = max_value - 1 if e == max_value-1 and cnt < 0 else e + cnt
        
        start_ret, end_ret = is_range(n_s, max_value), is_range(n_e, max_value)
        if not start_ret and not end_ret:
            return [-1, -1]
        elif not start_ret:
            return [0, n_e]
        elif not end_ret:
            return [n_s, max_value-1]
        else:
            return [n_s, n_e]
        
    s_y, e_y, s_x, e_x = x, x, y, y
    
    for dir, dx in reversed(queries):
        if dir == UP or dir == DOWN:
            if dir == DOWN:
                dx *= -1
            s_y, e_y = move(s_y, e_y, dx, n)
        
        if dir == LEFT or dir == RIGHT:
            if dir == RIGHT:
                dx *= -1
            s_x, e_x = move(s_x, e_x, dx, m)
        
        #print(s_y, e_y, s_x, e_x)
        if s_y == -1 or e_y == -1 or s_x == -1 or e_x == -1:
            return 0
    
    return (e_y - s_y + 1) * (e_x - s_x + 1)

#solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]])