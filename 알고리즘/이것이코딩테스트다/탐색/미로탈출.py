# 모든 노드를 방문하면서 방문했을때 이동거리를 기록한다.

from collections import deque

N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(list(map(int, input())))

visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs(arr, visited):
    queue = deque([0,0])
    visited[0][0] = 1
    while queue:
        y, x = queue.popleft(), queue.popleft()
        if(N > y+1 >= 0 and arr[y+1][x] == 1 and visited[y+1][x] == 0) :
            queue.append(y+1)
            queue.append(x)
            visited[y+1][x] = visited[y][x] + 1
        if(N > y-1 >= 0 and arr[y-1][x] == 1 and visited[y-1][x] == 0) :
            queue.append(y-1)
            queue.append(x)
            visited[y-1][x] = visited[y][x] + 1
        if(M > x+1 >= 0 and arr[y][x+1] == 1 and visited[y][x+1] == 0) :
            queue.append(y)
            queue.append(x+1)
            visited[y][x+1] = visited[y][x] + 1
        if(M > x-1 >= 0 and arr[y][x-1] == 1 and visited[y][x-1] == 0) :
            queue.append(y)
            queue.append(x-1)
            visited[y][x-1] = visited[y][x] + 1
            
bfs(arr, visited)
            
print(visited[N-1][M-1])
        
    
        