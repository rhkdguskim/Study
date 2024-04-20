# https://www.acmicpc.net/problem/1707

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(3e5))

T = int(input())

def dfs(node, group):
    visited[node] = group
    for new_node in edge[node]:
        if not visited[new_node]:
            if not dfs(new_node, group * -1):
                return False
        elif visited[new_node] == visited[node]:
            return False
    
    return True
        

for _ in range(T):
    V, E = map(int, input().split())
    edge = [set() for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        edge[u].add(v)
        edge[v].add(u)
        
    visited = [None] * (V+1)
    is_bipartite = True

    for i in range(1, V+1):
        if visited[i] is None:
            if not dfs(i, 1):
                is_bipartite = False
        
    if is_bipartite:
        print("YES")
    else:
        print("NO")
        

