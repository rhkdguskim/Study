# https://www.acmicpc.net/problem/1753
import heapq
V, E = map(int,input().split()) # 정점의 개수, 간선의 개수
K = int(input()) # 시작 정점의 번호
INF = 10e9
graph = [[] for _ in range(V+1)] # 두 정점사이의 관계를 나타내는 그래프
for _ in range(E): # 간선의 개수 만큼 입력을 받는다.
    a, b, c = map(int, input().split()) # a : 정점 b : 정점a와 연결된정점 c :간선의 길이
    graph[a].append([b,c]) # 정점a에 연결된 정점은 b이고 간선의 길이는 c의 정보를 추가한다.

distance = [INF for _ in range(V+1)] # 정점의 최단경로 값

def dijkstra(start):
    q = []    
    distance[start] = 0 # 자기를 방문한다. 거리 0
    heapq.heappush(q, [distance[start], start]) # 해당 노드의 최단경로값, 자기자신 인덱스
        
    while q:
        data, now = heapq.heappop(q)
        if distance[now] < data: # 이미 방문한 노드라면 패스
            continue
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, [cost, j[0]])
                
dijkstra(K)

for i in range(1, V+1): # 정점의 개수를 순회한다
    if distance[i] == INF :
        print("INF")
    else :
        print(distance[i])
            
