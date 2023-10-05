# https://www.acmicpc.net/problem/2468
from collections import deque
moves = ((0,1), (1,0), (0,-1), (-1,0))
N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
def divewater(depth):
    for i in range(N):
        for j in range(N):
            if depth >= graph[i][j]:
                visited[i][j] = True
                
def groupcount():
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                queue = deque()
                queue.append((i,j))
                visited[i][j] = True
                count += 1
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in moves:
                        ny = dy + y
                        nx = dx + x
                        if N > ny >= 0 and N > nx >= 0 and not visited[ny][nx]:
                            visited[ny][nx] = True
                            queue.append((ny,nx))
                            
    return count

ans = 0
for i in range(0, 101): # 아무 지역도 잠기지 않을수 있기때문에 0 부터 시작
    visited = [[False for _ in range(N)] for _ in range(N)]
    divewater(i)
    ans = max(groupcount(), ans)

print(ans)