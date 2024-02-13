# https://www.acmicpc.net/problem/17472
from collections import deque
move = [(1,0), (-1,0), (0,1), (0,-1)]
N, M = map(int, input().split()) # 세로, 가로
graph = [list(map(int, input().split())) for _ in range(N)]

def findGroup(i,j):
    for k in range(len(groupList)):
        for node in groupList[k]:
            if node[0] == i and node[1] == j:
                return k

def dfs(y,x, mode, cost): # 같은 그룹인지 체크하는 로직
    if graph[y][x] == 1: # 종료조건
        if cost == 1 or cost == 2:
            return None
        elif cost >= 3:
            return cost - 1, findGroup(y,x)
    
    dy, dx = move[mode]
    ny = dy + y
    nx = dx + x
    
    if N > ny >=0 and M > nx >=0:
        return dfs(ny,nx, mode, cost + 1)
    
    return None

def bfs(i,j):
    group = []
    queue = deque()
    if not visited[i][j] and graph[i][j] == 1:
        queue.append([i,j])
        group.append([i,j])
        visited[i][j] = True
        while queue:
            y , x = queue.popleft()
            for dy, dx in move:
                ny = dy + y
                nx = dx + x
                if N > ny >=0 and M > nx >=0 and not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append([ny,nx])
                    group.append([ny,nx])

        return group
    else:
        return None
    
def getParent(v1, parent):
    if v1 != parent[v1]:
        parent[v1] = getParent(parent[v1], parent)
    return parent[v1]
    
def union(v1,v2, parent):
    a = getParent(v1, parent)
    b = getParent(v2, parent)
    
    if a > b: # 더 작은 노드를 parent값을 선정한다.
        parent[a] = b
    else:
        parent[b] = a
        
groupList = []
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        result = bfs(i,j)
        if result != None:
            groupList.append(result)
    
nodegraph = []
for k in range(len(groupList)):
    for node in groupList[k]:
        y, x = node
        for i in range(4): # 가로,세로를 돌려본다
            result = dfs(y,x,i, 0)
            if result != None:
                nodegraph.append((result[0],k,result[1])) # cost, 시작, 종료
                
nodegraph.sort()
parent = [v1 for v1 in range(len(groupList))] # 자기자신을 부모노드로 초기화
result = 0
counter = 0
for cost, start, end in nodegraph:
    if getParent(start, parent) != getParent(end, parent):
        union(start, end, parent)
        result += cost
        counter += 1
        
if counter == len(groupList)-1: # 노드-1 의 개수와 간선의 개수가 같으면 최소신장트리 조건
    print(result)
else:
    print(-1)