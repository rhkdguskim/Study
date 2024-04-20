# https://www.acmicpc.net/problem/16234
import sys
from collections import deque
input = sys.stdin.readline
graph = []
N, L, R = map(int ,input().split())

for _ in range(N):
    graph.append(list(map(int, input().split())))
    
    


def bfs():
    visisted = [[False for _ in range(N)] for _ in range(N)]
    flag = False
    for i in range(N):
        for j in range(N):
            cnt = 0
            total = 0
            if not visisted[i][j]:
                visisted[i][j] = True
                queue = deque()
                city_group = []
                queue.append((i, j))
                city_group.append((i, j))
                while queue:
                    y, x = queue.popleft()
                    cnt += 1
                    total += graph[y][x]
                    for dy, dx in [(0,1), (1,0), (-1,0), (0,-1)]:
                        ny, nx = y + dy, x + dx
                        if N > ny>=0 and N > nx >= 0 and not visisted[ny][nx] and R >= abs(graph[y][x] - graph[ny][nx]) >= L:
                            visisted[ny][nx] = True
                            queue.append((ny, nx))
                            city_group.append((ny, nx))
            
                if cnt > 1:
                    flag = True
                    for cy, cx in city_group:
                        graph[cy][cx] = total // cnt

    
    return flag
            

ans = 0
while bfs():
    ans += 1

print(ans)