# https://www.acmicpc.net/problem/1774
# 최소 신장 트리
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

node = []
for _ in range(N):
    X, Y = map(int, input().split())
    node.append((X, Y))

parent = [i for i in range(N+1)]

def find(v1):
    if parent[v1] != v1:
        parent[v1] = find(parent[v1])
        return parent[v1]
    else:
        return v1

def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    
    if parent[p1] > parent[p2]:
        parent[p1] = parent[p2]
    else:
        parent[p2] = parent[p1]

def get_distance(y1, x1, y2, x2):
    return (pow(abs((y1-y2)), 2) + pow(abs(x1 - x2), 2)) ** 0.5
        
edge = []

for i in range(len(node)):
    for j in range(i+1, len(node)):
        if i != j:
            y1, x1 = node[i]
            y2, x2 = node[j]
            edge.append((get_distance(y1, x1, y2, x2), i+1, j+1))

edge.sort(key=lambda x:x[0])

for _ in range(M):
    X, Y = map(int, input().split())
    p1 = find(X)
    p2 = find(Y)
    if p1 != p2:
        union(p1, p2)

ans = 0.00
for cost, i, j in edge:
    p1 = find(i)
    p2 = find(j)
    if p1 != p2:
        ans += cost
        union(p1, p2)
        
ans = round(ans, 2)
print(f"{ans:.2f}")