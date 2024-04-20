# https://www.acmicpc.net/problem/11779

import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


n = int(input())
m = int(input())

edge = [[] for _ in range(n+1)]
reverse_edge = [[] for _ in range(n+1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    edge[s].append((e, cost))
    reverse_edge[e].append((s, cost))
    
start, end = map(int, input().split())


queue = []
dp = [INF for _ in range(n+1)]

heapq.heappush(queue, (start, 0))
while queue:
    cur, cost = heapq.heappop(queue)
    
    if cost > dp[cur]:
        continue
    
    dp[cur] = cost
    
    for next, next_cost in edge[cur]:
        new_cost = next_cost + cost
        if dp[next] > new_cost:
            dp[next] = new_cost
            heapq.heappush(queue, (next, new_cost))
    
                
city = []
city.append(end)
cur = end
while cur != start:
    for prev, cost in reverse_edge[cur]:
        if dp[cur] == dp[prev] + cost:
            city.append(prev)
            cur = prev
            break

print(dp[end])
print(len(city))  
print(*reversed(city))
