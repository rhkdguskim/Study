#https://www.acmicpc.net/problem/1005
# 1. 그래프를 만든다.
# 2. 루트노드를 찾는다.
# 3. 루트노드로부터 목적지 노드까지 방문하면서 시간을 구한다( 최소값을 갱신하고 최소값보다 커진다면 방문을 중단한다.)

T = int(input())
def findRoot(graph):
    visited = [False for _ in range(N)]
    for i in range(N):
        for node in graph[i+1]:
            visited[node-1] = True
            
    return visited.index(False) + 1

def dfs(node,cost, graph, d):
    global maxcost
    if node == W:
        maxcost = max(maxcost, cost)
    
    for newnode in graph[node]:
        dfs(newnode, cost + d[newnode], graph, d)

for _ in range(T):
    N, K = map(int, input().split()) # 건물의 개수, 건설순서의 규칙순서
    d = [0] + list(map(int, input().split())) # 건물당 건설에 걸리는 시간
    graph = [[] for _ in range(N+1)] # 해당 건물에서 갈 수 있는 규칙
    for _ in range(K): # 건설 순서 입력
        X, Y = map(int, input().split())
        graph[X].append(Y) # 1. 그래프를 만든다.
    
    W = int(input())
    maxcost = d[W-1] # 단일 노드일때로 초기화
    rootnode = findRoot(graph) # 2. 루트노드를 찾는다.
    dfs(rootnode, d[rootnode], graph, d)
    print(maxcost)
    