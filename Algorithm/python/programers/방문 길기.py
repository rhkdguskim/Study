# https://school.programmers.co.kr/learn/courses/30/lessons/49994
from collections import defaultdict

def solution(dirs):
    # U, D, R , L
    moves = {'U':(1, 0), 'D':(-1, 0), 'R':(0, 1), 'L':(0, -1)}
    visited = defaultdict(bool)
    start_y, start_x = 0, 0
    answer = 0
    
    for d in dirs:
        dy, dx = moves[d]
        ny, nx = start_y + dy, start_x + dx
        #print(ny, nx)
        if -5 <= ny <= 5 and -5 <= nx <= 5:
            if not visited[(start_y, start_x, ny, nx)]:
                visited[(start_y, start_x, ny, nx)] = True
                visited[(ny, nx, start_y, start_x)] = True
                answer += 1
                
            #print(start_y - 4, start_x - 4)
            start_y, start_x = ny, nx
    
    return answer