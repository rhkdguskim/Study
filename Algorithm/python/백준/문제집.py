# https://www.acmicpc.net/problem/1766
from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
in_degree = [0 for _ in range(N+1)]
edge = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    in_degree[b] += 1
    edge[a].append(b)
    
queue = []

for i in range(1, N+1):
    if in_degree[i] == 0:
        heappush(queue, i)
        
while queue:
    node = heappop(queue)
    
    print(node, end=' ')
    for new_node in edge[node]:
        in_degree[new_node] -= 1
        if in_degree[new_node] == 0:
            heappush(queue, new_node)

print()

