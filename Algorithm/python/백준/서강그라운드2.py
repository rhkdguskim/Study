# https://www.acmicpc.net/problem/14938
# 데이크스트라
import sys
import heapq

input = sys.stdin.readline

n, m, r = map(int, input().split())

items = list(map(int, input().split()))

edge = [[] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    edge[a].append((b, l))
    edge[b].append((a, l))
    
def dijikstra(start):
    queue = []
    INF = sys.maxsize
    distance = [INF for _ in range(n+1)]
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    score = items[start-1]
    while queue:
        cost, node = heapq.heappop(queue)

        if cost > distance[node]:
            continue
        
        if m >= cost and distance[node] > cost:
            score += items[node-1]
        
        distance[node] = cost
        
        for child, c in edge[node]:
            newcost = cost + c
            if distance[child] > newcost:
                heapq.heappush(queue, (newcost, child))
    
    return score

ans = 0
for i in range(1, n+1):
    ans = max(ans, dijikstra(i))
    
print(ans)