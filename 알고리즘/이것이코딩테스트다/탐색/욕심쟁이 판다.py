# https://www.acmicpc.net/problem/1937
# 판다는 대나무를 먹으면서 상하좌우로 이동하는데, 현재위치 보다 더 대나무 가 많온곳으로 갈수 있다.
# 판다가 최대한 많이 움직일 수 있는 수를 구하시오.
# 하나씩 방문해보면서 움직일 수 있는 최대 수를 구합니다. 해당 방문이 이미 이전값에서 방문한값이 있다면 최대 값이므로 백트래킹 합니다.
import sys
sys.setrecursionlimit(400000)
move = ((0,1), (0,-1), (1,0) , (-1,0))
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    

def dfs(i,j, visited):
    if visited[i][j]:
        return visited[i][j] + 1
    
    maxvalue = 1
    for dy, dx in move:
        ny = i + dy
        nx = j + dx
        if n > ny >=0 and n > nx >= 0: 
            if graph[ny][nx] > graph[i][j]: #  # 이미 방문한곳이 아니고 현재위치보다 먹이가 많다면
                if visited[ny][nx]:
                    distance = visited[ny][nx] + 1
                else:
                    distance = dfs(ny, nx, visited) + 1
                maxvalue = max(distance, maxvalue)
    
    visited[i][j] = maxvalue
    return visited[i][j]
        

visited = [[0 for _ in range(n)] for _ in range(n)]
maxvalue = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            distance = dfs(i,j, visited)
            maxvalue = max(distance, maxvalue)
            
            
print(maxvalue)