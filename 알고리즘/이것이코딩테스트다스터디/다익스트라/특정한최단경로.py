# https://www.acmicpc.net/problem/1504
import heapq
INF = int(10e9)
N, M = map(int, input().split()) # N 정점의개수, M 간선의 개수
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
v1, v2 = map(int, input().split())

distance = [INF] * (N+1)
distance2 = [INF] * (N+1)
def dijkstra(start, distance):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, [distance[start], start])
    
    while queue:
        dis, now  = heapq.heappop(queue)
        if(distance[now] < dis):
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, [distance[i[0]], i[0]])
                
dijkstra(v1, distance)
print(distance)
dijkstra(v2, distance2)
print(distance2)