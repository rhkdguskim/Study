# 구간1에서 구간2로 가는 길이를 0으로 모두 초기화 한다.
# 모든 그래프를 탐색하면서 쭉쭉 가면서 그래프를 갱신하는데 갱신하는 방법은 값이 나온값을 더한다.
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())
INF = sys.maxsize
graph = defaultdict(lambda : defaultdict(int))

for _ in range(N):
    a, b, c = map(str, input().split())
    c = int(c)
    graph[a][b] += c
    graph[b][a] += c
    
def bfs(src, dst, graph):
    path = defaultdict(int)
    visited = defaultdict(bool)
    queue = deque()
    queue.append(src)
    visited[src] = True
    while queue:
        u = queue.popleft()
        for v in graph[u].keys():
            if not visited[v] and graph[u][v] > 0:
                visited[v] = True
                queue.append(v)
                path[v] = u
    
    return visited[dst], path

ans = 0

while True:
    ret, path = bfs('A', 'Z', graph)
    if not ret:
        break
    
    min_dis = sys.maxsize
    
    dst = 'Z'
    while True:
        v = dst
        u = path[dst]
        min_dis = min(graph[u][v], min_dis)
        dst = u
        if dst == 'A':
            break
    
    dst = 'Z'
    while True:
        v = dst
        u = path[dst]
        graph[u][v] -= min_dis
        graph[v][u] += min_dis
        dst = u
        if dst == 'A':
            break
    
    ans += min_dis

print(ans)