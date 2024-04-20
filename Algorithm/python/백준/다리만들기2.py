# https://www.acmicpc.net/problem/17472
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
visited = [[False for _ in range(M)] for _ in range(N)]
group_name = 0
group = []

# 그룹이름으로 나누기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            group_name += 1
            queue = deque()
            queue.append((i, j))
            visited[i][j] = True
            graph[i][j] = group_name
            group.append([(i, j)])
            while queue:
                y, x = queue.popleft()
                for dy, dx in moves:
                    ny, nx = dy + y, dx + x
                    if N > ny >=0 and M > nx >=0 and graph[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        graph[ny][nx] = group_name
                        queue.append((ny, nx))
                        group[group_name-1].append((ny, nx))
                        

# 특정그룹에서 또다른 그룹까지의 간선정보 구하기
connect_info = []
for name, g in enumerate(group):
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque()
    for land in g:
        for dir in range(4):
            queue.append((land[0], land[1], 0, dir))
        visited[land[0]][land[1]] = True
    while queue:
        y, x, cost, d = queue.popleft()
        ny, nx = moves[d][0] + y, moves[d][1] + x
        
        if N > ny >=0 and M > nx >=0 and not visited[ny][nx]:
            visited[ny][nx] = True
            if graph[ny][nx] == 0:
                queue.append((ny, nx, cost + 1, d))
            else:
                if (name+1 , graph[ny][nx], cost) not in connect_info and cost != 1:
                    connect_info.append((name +1, graph[ny][nx], cost))
                    


parent = [i for i in range(len(group))]

def find(a):
    if a != parent[a]:
        v = find(parent[a])
        return v
    else:
        return a

def union(a, b):
    v1 = find(a)
    v2 = find(b)
    if v1 > v2:
        parent[v1] = v2
    else:
        parent[v2] = v1
        
connect_info.sort(key=lambda x:x[2])

ans = 0
con_cnt = 0
for v1, v2, cost in connect_info:
    p1, p2 = find(v1-1), find(v2-1)
    if p1 != p2:
        con_cnt += 1
        ans += cost
        union(v1-1, v2-1)
    

if con_cnt == len(group) -1:
    print(ans)
else:
    print(-1)