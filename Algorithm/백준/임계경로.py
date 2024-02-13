# https://www.acmicpc.net/problem/1948
'''
5
7
1 2 1
1 3 3
2 3 2
2 4 1
2 5 3
3 5 1
4 5 1
1 5

5
7
1 2 1
1 3 3
2 3 2
2 4 1
4 5 1
3 5 1
2 5 3
1 5
'''

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

in_degree = [0 for _ in range(n+1)]
distance = [0 for _ in range(n+1)]
edge = [[] for _ in range(n+1)]
r_edge = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    edge[start].append((end, cost))
    r_edge[end].append((start, cost))
    in_degree[end] += 1
    
start , end = map(int, input().split())
queue = deque()
queue.append((start, 0))

while queue:
    node, cost = queue.pop()
    
    for new_node, dst_cost in edge[node]:
        distance[new_node] = max(distance[new_node], cost + dst_cost)
        in_degree[new_node] -= 1
        if in_degree[new_node] == 0:
            queue.append((new_node, distance[new_node]))

queue = deque()
queue.append(end)
visited = [[False for _ in range(n+1)] for _ in range(n+1)]

cnt = 0
while queue:
    node = queue.pop()
    
    for new_node, new_cost in r_edge[node]:
        if distance[node] - new_cost == distance[new_node]:
            if not visited[node][new_node]:
                visited[node][new_node] = True
                cnt += 1
                queue.append(new_node)

print(distance[end])
print(cnt)

