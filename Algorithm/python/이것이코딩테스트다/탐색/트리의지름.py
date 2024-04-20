# https://www.acmicpc.net/problem/1967
# 트리의 지름을 구하는 방법은 하나의 노드로부터 깊이우선탐색하여 제일 깊은 노드를 찾고
# 제일 깊은 노드로부터 또 다른 제일 깊은 노드까지 길이를 찾으면 된다.
import sys
sys.setrecursionlimit(10001)

n = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(node, cost):
    global max_distance, farthest_node
    visited[node] = True
    if cost > max_distance:
        max_distance = cost
        farthest_node = node
    for v1, distance in graph[node]:
        if not visited[v1]:
            dfs(v1, cost + distance)

max_distance = -1
farthest_node = 0
visited = [False for _ in range(n+1)]
dfs(1, 0)  # 첫 번째 DFS

visited = [False for _ in range(n+1)]
max_distance = -1
dfs(farthest_node, 0)  # 두 번째 DFS

print(max_distance)