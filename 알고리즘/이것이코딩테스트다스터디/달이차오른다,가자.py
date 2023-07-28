# https://www.acmicpc.net/problem/1194
from collections import deque
from pprint import pprint
N, M = map(int, input().split()) # 세로, 가로
move = [(0,1), (0,-1), (1,0), (-1,0)]
key = ('a', 'b', 'c', 'd', 'e', 'f')
door =  ('A', 'B', 'C', 'D', 'E', 'F')
start = []
graph = []
for i in range(N):
    char = input()
    for j in range(M):
        if char[j] == '0':
            start.append(i)
            start.append(j)
    graph.append(char)
    
pprint(graph[0][0])

keylist = []
mincost = int(1e9)
def bfs():
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append([start[0], start[1], 0])
    visited[start[0]][start[1]] = True
    keyhash = dict()
    nextqueue = []
    isFinished = False
    while queue:
        i , j, cost = queue.popleft()
        for dy, dx in move:
            ny, nx = i + dy, j + dx
            if N > ny >= 0 and M > nx >= 0:
                if graph[ny][nx] == '.' and not visited[ny][nx]: # .인경우 방문후 더 탐색
                    visited[ny][nx] = True
                    queue.append([ny, nx , cost + 1])
                elif graph[ny][nx] == '1' and not visited[ny][nx]: # 1인경우 방문후 최소값 갱신
                    visited[ny][nx] = True
                    if mincost > cost + 1:
                        mincost = cost + 1
                elif graph[ny][nx] in key and not visited[ny][nx]:
                    visited[ny][nx] = True
                    keyhash[graph[ny][nx]] = cost + 1
                    queue.append([ny, nx , cost + 1])
                elif graph[ny][nx] in door and not visited[ny][nx]:
                    if graph[ny][nx] in keylist:
                        visited[ny][nx] = True
                        queue.append([ny, nx , cost + 1])
                    else:
                        nextqueue.append([ny,nx, cost + 1])
                        
    return keyhash, nextqueue

print(bfs())