# https://www.acmicpc.net/problem/1504
# 1) 1-> V1에서 v2최소거리 -> 나머지노드
# 2) 1-> v2에서 v1최소거리 -> 나머지노드
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
distance3 = [INF] * (N+1)
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


dijkstra(v1, distance) # V1에서 나머지노드까지 최소거리
dijkstra(v2, distance2) # v2에서 나머지노드까지 최소거리
dijkstra(1, distance3) # 1에서 나머지노드까지 최소거리

minvalue = INF

for i in range(N):
    if i != 1:
        minvalue = min(minvalue, distance3[v1] + distance[v2] + distance2[i], distance3[v1] + distance2[v2] + distance[i])
    
if minvalue == INF:
    print(-1)
else:
    print(minvalue)