#https://www.acmicpc.net/problem/1238
import sys
import heapq

input = sys.stdin.readline
INF = int(1e15)

N, M, X = map(int, input().split())

edge = [[] for _ in range(N+1)]
r_edge = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    edge[start].append((end, cost))
    r_edge[end].append((start, cost))

distance = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    distance[i][i] = 0

queue = []
for node, cost in edge[X]:
    heapq.heappush(queue, (node, cost))

while queue:
    n, cost = heapq.heappop(queue)
    if cost > distance[X][n]:
        continue
    
    distance[X][n] = cost
    
    for n_n, n_cost in edge[n]:
        new_cost = n_cost + cost
        if distance[X][n_n] > new_cost:
            heapq.heappush(queue, (n_n, new_cost))
    
        

queue = []
for node, cost in r_edge[X]:
    heapq.heappush(queue, (node, cost))

while queue:
    n, cost = heapq.heappop(queue)
    if cost > distance[n][X]:
        continue
    
    distance[n][X] = cost
    
    for n_n, n_cost in r_edge[n]:
        new_cost = n_cost + cost
        if distance[n_n][X] > new_cost:
            heapq.heappush(queue, (n_n, new_cost))
        
ans = 0
for i in range(1, N+1):
    ans = max(ans, distance[i][X] + distance[X][i])
    #print(i, distance[i][X] + distance[X][i])

print(ans)