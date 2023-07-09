#https://www.acmicpc.net/problem/2206
from collections import deque
N, M = map(int, input().split()) # 세로, 가로
INF = int(10e9)
table = []
x = [0, 0, 1, -1]
y = [1, -1, 0, 0] 
for _ in range(N):
    char = str(input())
    table.append(list(map(int, char)))
    
visited = [[[INF for _ in range(M)] for _ in range(N)] for _ in range(2)]
queue = deque()
queue.append([0,0, True, 1])
while queue:
    i,j,canbreak,depth = queue.popleft()
    temp = 0
    if canbreak:
        temp=1
    else:
        temp=0
    if visited[temp][i][j] > depth:
        if table[i][j] == 0:
            visited[temp][i][j] = depth
            for k in range(4):
                dy = y[k] + i 
                dx = x[k] + j
                if N > dy >= 0 and M > dx >=0:
                    queue.append([dy,dx,canbreak,depth+1])
            
        elif table[i][j] == 1 and canbreak:
            visited[temp][i][j] = depth
            canbreak = False
            for k in range(4):
                dy = y[k] + i 
                dx = x[k] + j
                if N > dy >= 0 and M > dx >=0 and table[dy][dx] == 0:
                    queue.append([dy,dx,canbreak,depth+1])

if visited[0][N-1][M-1] == INF and visited[1][N-1][M-1] == INF:
    print(-1)
elif visited[0][N-1][M-1] != INF:
    print(visited[0][N-1][M-1])
else:
    print(visited[1][N-1][M-1])