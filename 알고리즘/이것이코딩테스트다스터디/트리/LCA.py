#https://www.acmicpc.net/problem/11437
N = int(input()) # 노드의 개수
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a ,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
M = int(input()) # 쌍의 개수

#print(graph)
nodepair = []
for _ in range(M):
    a, b = map(int, input().split())
    nodepair.append([a,b])
    

def dfs(node, v1, v2, rootnode):
    global v1found
    global v2found
    global init
    # 재귀 종료 조건 방문한 노드가 v1 이거나 v2일경우
    if node == v1:
        v1found = True
        
    if node == v2:
        v2found = True
    
    for newnode in graph[node]:
        if newnode != rootnode:
            rootnode = node
            dfs(newnode, v1, v2, rootnode)
            if v1found and v2found and init:
                init = False
                print(node)
                return True
        
    
for v1, v2 in nodepair:
    v1found = False
    v2found = False
    init = True
    dfs(1, v1, v2, 0)