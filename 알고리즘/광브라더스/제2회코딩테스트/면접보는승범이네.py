# https://www.acmicpc.net/problem/17835
import sys
import heapq
from pprint import pprint
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    U, V, C = map(int, input().split())
    heapq.heappush(graph[U], (C, V))
    heapq.heappush(graph[V], (C, U))

ic = list(map(int, input().split()))

maxidx = 0
maxdistance = 0
visited = [[-1 for _ in range(N+1)] for _ in range(N+1)]
queue = []

for k in ic:
    heapq.heappush(queue, (0, k, k))
    visited[k][k] = 0

while queue:
    cost, source, target = heapq.heappop(queue)

    while graph[target]:
        dis, newidx = heapq.heappop(graph[target])
        if visited[source][newidx] == -1:
            visited[source][newidx] = cost + dis
            heapq.heappush(queue, (dis + cost, source, newidx))

pprint(visited)





