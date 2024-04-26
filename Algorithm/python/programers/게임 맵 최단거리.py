# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque

def solution(maps):
    queue = deque()
    height = len(maps)
    width = len(maps[0])
    
    visited = [[False]*width for _ in range(height)]
    
    visited[0][0] = True
    queue.append((0, 0, 1))
    
    while queue:
        i, j, cost = queue.popleft()
        
        if i == height-1 and j == width-1:
            return cost
        
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = dy + i, dx + j
            if height > ny >= 0 and width > nx >= 0 and maps[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx , cost + 1))
                
    return -1