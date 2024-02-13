#https://www.acmicpc.net/problem/2573
from collections import deque
N, M = map(int, input().split()) # 세로, 가로

graph = [list(map(int, input().split())) for _ in range(N)]
move = [(0,1), (0,-1), (1,0), (-1,0)]
def oneYearsGo():
    value = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                for dy,dx in move:
                    ny = dy + i
                    nx = dx + j
                    if N > ny >=0 and M > nx >=0 and graph[ny][nx] == 0: # 주변이 바다라면
                        value[i][j] += 1 # 녹인다.
                        
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                graph[i][j] = max(0, graph[i][j] - value[i][j])
    
    return 1

def bfs(i,j):
    queue = deque()
    if graph[i][j] > 0 and not visited[i][j]: # 빙산이라면
        queue.append((i,j))
        visited[i][j] = True
        while queue:
            y, x = queue.popleft()
            for dy,dx in move:
                ny = dy + y
                nx = dx + x
                if N > ny >=0 and M > nx >=0 and graph[ny][nx] > 0 and not visited[ny][nx]: # 주변이 빙산이라면
                    visited[ny][nx] = True
                    queue.append((ny,nx))
        
        return 1
    else:
        return 0
    
years = 0
while True:
    count = 0
    oneYearsGo()
    years += 1
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            count += bfs(i,j)
    if count >= 2 or count ==0:
        if count == 0:
            print(0)
        else:
            print(years)
        break