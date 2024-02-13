#https://www.acmicpc.net/problem/1922
N = int(input()) # 정점의개수
M = int(input()) # 간선의개수
parent = [v1 for v1 in range(N+1)]
graph = []
for _ in range(M):
    a,b,cost = map(int, input().split())
    graph.append([cost, a, b])
    
graph.sort()

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    
    return parent[a]

def union(v1,v2):
    a = find(v1)
    b = find(v2)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

result = 0
for cost, a ,b in graph:
    if (find(a) != find(b)):
        union(a,b)
        result += cost
        
print(result)
    

