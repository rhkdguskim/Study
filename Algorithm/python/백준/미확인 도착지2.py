# https://www.acmicpc.net/problem/9370
# 데이크스트라로 방문거리를 체크 한다.
# 이제 후보들에서 도착지까지 거꾸로 탐색하면서 
# g, h 경로를 지나가는 경우를 찾아서 후보에 추가한다.

import sys
import heapq

input = sys.stdin.readline

def dijikstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cost, node = heapq.heappop(queue)
        
        if distance[node] < cost:
            continue
        
        distance[node] = cost
        
        for child, c in edge[node]:
            new_cost = c + cost
            if distance[child] > new_cost:
                distance[child] = new_cost
                heapq.heappush(queue, (new_cost, child))
    
    return distance

T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    INF = sys.maxsize
    s, g, h = map(int, input().split())
    edge = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        edge[a].append((b, d))
        edge[b].append((a, d))
        
    d_s = dijikstra(s)
    d_h = dijikstra(h)
    d_g = dijikstra(g)
    
    result = []
    for _ in range(t):
        e = int(input())
        if (d_s[h] + d_h[g] + d_g[e] == d_s[e]) or (d_s[g] + d_g[h] + d_h[e] == d_s[e]):
            result.append(e)
    
    print(*sorted(result))