# https://www.acmicpc.net/problem/16947
# 사이클까지의 최소거리를 구한다.
# 사이클이 존재한다면 0, 주변에 사이클이 있는 가장 가까운 노드를 찾는다.
# 사이클이 생기는 조건은 DFS 탐색했을때 방문한 배열이 있다면 사이클이 생기고 그 방문 배열들은 모두 사이클 처리를 한다.

import sys
input = sys.stdin.readline

N = int(input())
edge = [[] for _ in range(N+1)]

for _ in range(N):
    start, end = map(int, input().split())
    edge[end].append(start)
    edge[start].append(end)
    
cycled = [False for _ in range(N+1)]

def dfs(node, nodes:set, cur):
    if len(nodes) > 2 and cur == node:
        for v in nodes:
            cycled[v] = True
        return
    
    for child in edge[node]:
        new_node = child
        if visited[node][new_node] == False:
            visited[node][new_node] = True
            visited[new_node][node] = True
            nodes.add(new_node)
            dfs(new_node, nodes, cur)
            nodes.remove(new_node)
            visited[node][new_node] = False
            visited[new_node][node] = False


for i in range(1, N+1):
    visited = [[False for _ in range(N+1)] for _ in range(N+1)]
    if not cycled[i]:
        dfs(i, set([i]), i)

print(cycled)