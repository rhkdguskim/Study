# https://www.acmicpc.net/problem/1707
# A구역과 B구역으로 나눈다.
# A구역에 추가할때, 해당 노드가 A와 인접한 노드가 있는지 확인한다. 없다면 추가한다.
# B구역에 추가할때, 해낭 노드가 B와 인접한 노드가 있는지 확인한다. 없다면 추가한다.
# 위의 두조건이 만족하지 않을경우 이분 그래프를 만들 수 없다.

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

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
            queue = deque()
            visited[i] = 1
            queue.append(i) # i번 노드, 구역 A
            while queue:
                node = queue.popleft()
                
                for new_node in edge[node]:
                    if visited[new_node] is None:
                        visited[new_node] = visited[node] * -1
                        queue.append(new_node)
                    else:
                        if visited[new_node] == visited[node]:
                            is_bipartite = False
                            break
        
        if not is_bipartite:
            break
        
    if is_bipartite:
        print("YES")
    else:
        print("NO")
