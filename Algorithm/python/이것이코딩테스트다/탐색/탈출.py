# https://www.acmicpc.net/problem/3055

from copy import deepcopy
from collections import deque
from pprint import pprint
R ,C = map(int, input().split()) # R행 C열
move = ((0,1), (0,-1), (1,0), (-1,0))
graph = []
start = [0,0]
end = [0,0]
for i in range(R):
    char = list(input())
    for j in range(C):
        if char[j] =='D': # 비버 동굴 위치
            end = [i,j]
        elif char[j] == 'S': # 너구리 위치
            start = [i,j]
            
    graph.append(char)
    

def bfs(arr, queue):
    while queue:
        y,x, cost = queue.popleft()
        for dy, dx in move:
            ny = dy + y
            nx = dx + x
            if R > ny >=0 and C > nx >= 0 and not visited[ny][nx] and graph[ny][nx] == '.':
                queue.append((ny,nx, cost + 1))
                arr[ny][nx] = cost + 1
                visited[ny][nx] = True
INF = int(10e6)
water = [[INF for _ in range(C)] for _ in range(R)]
baccon = [[INF for _ in range(C)] for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]
queue = deque()
for i in range(R):
    for j in range(C):
        if graph[i][j] == '*':
                visited[i][j] = True
                queue.append([i,j,0])

bfs(water, queue)
visited = [[False for _ in range(C)] for _ in range(R)]
queue = deque()
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
                visited[i][j] = True
                queue.append((i,j,0))
                
bfs(baccon, queue)

for i in range(R):
    for j in range(C):
        if water[i][j] > baccon[i][j]:
            graph[i][j] = '.'
        else:
            graph[i][j] = '*'
                
                
y1,x1 = start
y2, x2 = end
graph[y1][x1] = '.'
graph[y2][x2] = '.'

visited = [[False for _ in range(C)] for _ in range(R)]
visited [y1][x1] = True
queue.append((y1, x1, 0))
bfs(graph, queue)
if graph[y2][x2] == '.':
    print('KAKTUS')
else:
    print(graph[y2][x2])