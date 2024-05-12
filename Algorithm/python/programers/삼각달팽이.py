# https://school.programmers.co.kr/learn/courses/30/lessons/68645
from itertools import chain

def solution(n):
    move = [(1, 0), (0, 1), (-1, -1)]
    
    def change_pos(pos):
        if pos == 2:
            return 0
        else:
            return pos + 1
        
    temp = [[0] * (i+1) for i in range(n)]
    pos = 0
    y, x = 0, 0
    start = 1
    for i in range(n, 0, -1):
        temp[y][x] = start
        for _ in range(i-1):
            start += 1
            y, x = y + move[pos][0], x + move[pos][1]
            temp[y][x] = start
        
        pos = change_pos(pos)
        y, x = y + move[pos][0], x + move[pos][1]
        start += 1
                
    return list(chain(*temp))

solution(3)