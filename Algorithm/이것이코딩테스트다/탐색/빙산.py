# https://www.acmicpc.net/problem/2573
from pprint import pprint
from collections import deque
N, M = map(int, input().split()) # 세로, 가로
graph = []
move = [(0,1), (0,-1), (1,0), (-1,0)]
for i in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)
    
years = 0
isallSea = False
def oneYearsgo():
    updatetable = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                for k in range(4):
                    dy = move[k][0] + i
                    dx = move[k][1] + j
                    if N > dy >=0 and M > dx >=0 and graph[dy][dx] == 0: # 바다이면
                        updatetable[i][j] += 1
                        
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                graph[i][j] -= updatetable[i][j]
                
    return 1
            
    
def isValied():
    visited = [[False for _ in range(M)] for _ in range(N)]
    groupcount = 0
    global isallSea
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not visited[i][j]:
                queue = deque()
                groupcount += 1
                queue.append([i,j])
                visited[i][j] = True
                while queue:
                    i,j = queue.popleft()
                    for k in range(4):
                        dy = move[k][0] + i
                        dx = move[k][1] + j
                        if N > dy >=0 and M > dx >=0:
                            if graph[dy][dx] > 0 and not visited[dy][dx]: # 빙산이고 방문하지 않았다면 방문한다.
                                visited[dy][dx] = True
                                queue.append([dy,dx])
    if groupcount == 0:
        isallSea = True
    return groupcount >= 2 or groupcount == 0 # 그룹이 2개 이상이거나 아예 없는경우(전부 바다인경우)


while True:
    years += oneYearsgo()
    if isValied():
        break
    
if isallSea:
    print(0)
else:
    print(years)