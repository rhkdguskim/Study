# https://www.acmicpc.net/problem/2146
# bfs 탐색을 통하여 그룹핑을 한다.
# 각각의 그룹에서 시작하여 다른 그룹까지의 거리를 계산한다. ( 모든경우의 수 )
# 모든 경우의 수를 최소값을 구한다.
INF = int(10e9)
from collections import deque
from pprint import pprint
move = ((1,0), (-1,0), (0,1), (0,-1))
N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    

def getDistance(i,j):
    global min_distance
    visited[i][j] = True
    queue = deque()
    queue.append((i,j, 0))
    myGroup = graph[i][j]
    while queue:
        y,x, cost = queue.popleft()
        for dy, dx in move:
            ny = dy + y
            nx = dx + x
            if N > ny >=0 and N > nx >= 0 and graph[ny][nx] != myGroup: # 자기자신의 그룹이 아니라면 방문하여
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if graph[ny][nx] == 0 and min_distance > cost + 1: # 바다라면 계속 방문한다. 앞으로 방문해도 더 작은 값이라면 방문가능
                        queue.append((ny, nx, cost + 1))
                    elif graph[ny][nx] != 0:
                        min_distance = min(cost, min_distance)

def byGroup(i,j):
    global groupLabel
    groupLabel += 1
    
    graph[i][j] = groupLabel
    visited[i][j] = True
    queue = deque()
    queue.append((i,j))
    while queue:
        y,x = queue.popleft()
        for dy, dx in move:
            ny = dy + y
            nx = dx + x
            if N > ny >=0 and N > nx >= 0 and graph[ny][nx] != 0: # 바다가 아니라면 그룹핑을 한다.
                if not visited[ny][nx]:
                    graph[ny][nx] = groupLabel
                    visited[ny][nx] = True
                    queue.append((ny, nx))


visited = [[False for _ in range(N)] for _ in range(N)]
groupLabel = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0 and not visited[i][j]:
            byGroup(i,j)

min_distance = INF

for i in range(N):
    for j in range(N):
        visited = [[False for _ in range(N)] for _ in range(N)]
        if graph[i][j] != 0 and not visited[i][j]:
            
            getDistance(i,j)
            
print(min_distance)