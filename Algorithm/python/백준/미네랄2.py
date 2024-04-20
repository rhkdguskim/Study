# https://www.acmicpc.net/problem/18500
import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(str(input().strip())) for _ in range(R)]
N = int(input())
arrow = list(map(int, input().split()))

toggle = False # false가 왼쪽, true 가 오른쪽

def attack(h, dir):
    start = 0
    if dir:
        start = C-1
        
    while C > start >=0 and graph[h][start] == '.':
        if dir:
            start -= 1
        else:
            start += 1
            
    if C > start >=0 and graph[h][start] == 'x':
        graph[h][start] = '.'

def find_air_mineral():
    groups = []
    visited = [[False for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'x' and not visited[i][j]:
                visited[i][j] = True
                queue = deque()
                temp = []
                is_land = False
                queue.append((i, j))
                temp.append((i, j))
                while queue:
                    y, x = queue.popleft()
                    if y == R-1:
                        is_land = True
                    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        ny, nx = y + dy, x + dx
                        if R > ny >= 0 and C > nx >= 0 and not visited[ny][nx] and graph[ny][nx] == 'x':
                            visited[ny][nx] = True
                            temp.append((ny, nx))
                            queue.append((ny, nx))
                
                if not is_land:
                    groups.append(temp)
                
    return groups
    
def move(group):
    queue = deque()
    for q in group:
        queue.append((q[0], q[1], 0))
        graph[q[0]][q[1]] = '.'
        
    while queue:
        y, x, cost = queue.popleft()
        
        if y == R-1 or graph[y+1][x] == 'x':
            for n_y, n_x in group:
                graph[n_y + cost][n_x] = 'x'
            break
                
        queue.append((y+1, x, cost + 1))
            
for i in range(N):
    attack(R-arrow[i], toggle)
    toggle = not toggle
        
    groups = find_air_mineral()
    for group in groups:
        move(group)

for p in graph:
    print(''.join(p))