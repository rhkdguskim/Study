# https://www.acmicpc.net/problem/1197
V, E = map(int, input().split())
parent = [v1 for v1 in range(V+1)] # 정점의 개수만큼 생성

def find(v1):
    if v1 !=parent[v1]:
        parent[v1] = find(parent[v1])
        
    return parent[v1]

def union(a, b):
    a = find(a)
    b = find(b)

    # 작은 루트 노드를 기준으로 합침
    if b < a:
        parent[a] = b
    else:
        parent[b] = a
        
graph = []
for _ in range(E): # 간선의 개수
    a, b ,c = map(int, input().split())
    graph.append([c, a, b])

graph.sort()

result = 0
for cost, a , b in graph:
    if find(a) != find(b):
        union(a, b)
        result += cost

print(result)
    