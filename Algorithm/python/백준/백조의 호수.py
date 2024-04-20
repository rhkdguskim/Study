# https://www.acmicpc.net/problem/3197

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

table = [list(str(input().strip())) for _ in range(R)]

def move_bird(queue : deque, visited : list):
    new_queue = deque()
    
    while queue:
        y, x = queue.popleft()
        
        if swan[1][0] == y and swan[1][1] == x:
            return True, None
        
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = dy + y, dx + x
            if R > ny >=0 and C > nx >= 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                
                if table[ny][nx] == '.':
                    queue.append((ny, nx))
                else:
                    new_queue.append((ny, nx))
                    
    return False, new_queue

def melt(water):
    new_water = deque()
    queue = deque(water)
    
    while queue:
        y, x = queue.popleft()
        
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = dy + y, dx + x
            if R > ny >=0 and C > nx >= 0:
                if table[ny][nx] == 'X':
                    table[ny][nx] = '.'
                    new_water.append((ny, nx))
                    
    return new_water

swan = deque()
water = deque()

for i in range(R):
    for j in range(C):
        if table[i][j] == 'L':
            table[i][j] = '.'
            swan.append((i, j))
            water.append((i, j))
        if table[i][j] == '.':
            water.append((i, j))

queue = deque([(swan[0][0], swan[0][1])])

visited = [[False for _ in range(C)] for _ in range(R)]
visited[swan[0][0]][swan[0][1]] = True

day = 0
while True:
    is_found, queue = move_bird(queue, visited)
    if is_found:
        break
    
    water = melt(water)
    day += 1

print(day)