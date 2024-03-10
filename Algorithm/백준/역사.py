# https://www.acmicpc.net/problem/1613

# 위상정렬문제인가?
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, k = map(int, input().split())

distance = [set() for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
edge = [[] for _ in range(n+1)]
for _ in range(k):
    s, e = map(int, input().split())
    in_degree[e] += 1
    edge[s].append(e)

def dfs(node):
    for child in edge[node]:
        in_degree[child] -= 1
        distance[child] |= distance[node]
        if in_degree[child] == 0:
            distance[child].add(child)
            dfs(child)
            
root = []
for i in range(1, n+1):
    if in_degree[i] == 0:
        distance[i].add(i)
        root.append(i)

for i in root:
    dfs(i)
    
s = int(input())
for _ in range(s):
    s, e = map(int, input().split())
    if s in distance[e]:
        print(-1)
    elif e in distance[s]:
        print(1)
    else:
        print(0)
        