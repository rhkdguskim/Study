# https://www.acmicpc.net/problem/1939
import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

edge = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    edge[A].append((B, C))
    edge[B].append((A, C))

for i in range(1, N):
    edge[i].sort(key=lambda x:-x[1])
            
start, end = map(int, input().split())
queue = []
heapq.heappush(queue, (0, start))

dp = [-1 for _ in range(N+1)]

while queue:
    cost, src = heapq.heappop(queue)
    cost = -1 * cost
    
    if src == end:
        print(cost)
        break
    
    if dp[src] > cost:
        continue
    
    dp[src] = cost
    
    for dst, n_cost in edge[src]:
        if cost == 0:
            dp[dst] = cost
            heapq.heappush(queue, (-n_cost, dst))
        else:
            n_cost = min(n_cost, cost)
            if n_cost > dp[dst]:
                heapq.heappush(queue, (-n_cost, dst))