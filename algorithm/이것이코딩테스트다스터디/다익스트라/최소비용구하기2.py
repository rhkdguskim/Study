# https://www.acmicpc.net/problem/1916
import heapq
INF = int(10e9)
N = int(input()) # 도시의 개수 ( 정점의 개수 )
M = int(input()) # 버스의 개수 ( 간선의 개수 )
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end , cost = map(int, input().split())
    graph[start].append([end, cost]) # 끝, 비용
    
start , end = map(int, input().split())

distance = [INF for _ in range(N+1)]
queue = []
distance[start] = 0
heapq.heappush(queue, [distance[start], start])

while queue:
    cost, city = heapq.heappop(queue)
    if distance[city] > cost:
        continue
    
    for city2, cost2 in graph[city]:
        if distance[city2] > cost2 + cost:
            distance[city2] = cost2 + cost
            heapq.heappush(queue, [distance[city2], city2])
            
print(distance[end])