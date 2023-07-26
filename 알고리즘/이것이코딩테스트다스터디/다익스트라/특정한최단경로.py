# https://www.acmicpc.net/problem/1504
# 1) 1-> V1 -> V2 -> 노드 N
# 2) 1-> V2 -> V1 -> 노드 N
import heapq
INF = int(10e9)
N, M = map(int, input().split()) # N 정점의개수, M 간선의 개수
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
v1, v2 = map(int, input().split())


def dijkstra(start, end):
    distance = [INF] * (N+1)
    queue = []
    distance[start] = 0
    heapq.heappush(queue, [distance[start], start])
    
    while queue:
        dis, now  = heapq.heappop(queue)
        if dis > distance[now]: # 방문하고자하는 거리가 이미 최소값인 경우 방문하지 않는다.
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if distance[i[0]] > cost: # 자기자신의 가중치를 더하고 방문했을때 이미 최소값인경우 또 한 방문하지 않는다.
                distance[i[0]] = cost
                heapq.heappush(queue, [distance[i[0]], i[0]])
                
    return distance[end]

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if path1 >= INF and path2 >= INF: # 방문 할 수 없는경우
    print(-1)
else:
    print(min(path1, path2))