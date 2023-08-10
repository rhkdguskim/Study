# https://www.acmicpc.net/problem/2589
# 육지의 그룹을 분리한다( 너비우선 탐색 )
# 각각의 그룹으로부터 2개의 조합을 만들어 최단거리를 구한다. 그 최단 거리중 가장 큰 값을 return 하면 정답
from collections import deque
from itertools import combinations

N, M = map(int, input().split()) # 세로, 가로
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
graph = [list(input()) for _ in range(N)]

# 그룹별 좌표를 반환하는 함수
def getGroup():
    groupList = []
    visited = [[False] * M for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'L' and not visited[i][j]:
                group = []
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                group.append((i, j))
                
                while queue:
                    y, x = queue.popleft()
                    
                    for dy, dx in move:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and graph[ny][nx] == 'L':
                            visited[ny][nx] = True
                            queue.append((ny, nx))
                            group.append((ny, nx))
                
                groupList.append(group)
                
    return groupList

# 미리 모든 정점 간 거리를 계산한 후 메모이제이션
distance = [[[[float('inf')] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            queue = deque()
            queue.append((i, j, 0))
            distance[i][j][i][j] = 0
            
            while queue:
                y, x, cost = queue.popleft()
                
                for dy, dx in move:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 'L' and distance[i][j][ny][nx] == float('inf'):
                        distance[i][j][ny][nx] = cost + 1
                        queue.append((ny, nx, cost + 1))

grouplist = getGroup()
maxvalue = 0

# 그룹 내의 노드 쌍에 대한 최단 거리 계산
for group in grouplist:
    for a, b in combinations(group, 2):
        maxvalue = max(maxvalue, distance[a[0]][a[1]][b[0]][b[1]])

print(maxvalue)