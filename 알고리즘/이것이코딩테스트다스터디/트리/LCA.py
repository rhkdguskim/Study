#https://www.acmicpc.net/problem/11437
import sys
sys.setrecursionlimit(int(1e5))
N = int(input()) # 노드의 개수
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a ,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
M = int(input()) # 쌍의 개수

d = [0 for _ in range(N+1)]
c = [False for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

def dfs(rootnode, depth):
    d[rootnode] = depth
    c[rootnode] = True
    for childnode in graph[rootnode]:
        if not c[childnode]:
            parent[childnode] = rootnode
            dfs(childnode, depth+1)
            
            
def lca(a,b):
    # 노드의 깊이를 서로 맞춘다.
    while d[a] != d[b]: # a가 b보다 깊이가 큰경우
        if d[a] > d[b]:
            a = parent[a] # a가 거슬러 올라간다.
        else:
            b = parent[b] # b가 거슬로 올라간다.
            
    while a != b:
        a = parent[a]
        b = parent[b]
        
    return a

dfs(1,0)

for i in range(M):
    a, b = map(int, input().split())
    print(lca(a,b))