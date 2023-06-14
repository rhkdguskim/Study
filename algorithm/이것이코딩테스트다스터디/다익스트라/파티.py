import heapq
N,M,X = map(int, input().split()) # N 마을수, M 도로수, X = 파티시작위치
INF = 10e9
graph = [[] for _ in range(N+1)] # 마을의 수만큼 그래프 생성
for _ in range(M) : # 도로수 즉, 간선의 수만큼 입력을 받는다
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

distance = [INF] * (N+1)
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q,[start,0])
    while q:
        new, dis = heapq.heappop(q)
        if(distance[new] < dis): # 이미 구한 값이라면 SKIP!!
            continue
        for i in graph[new]:
            cost = distance[new] + i[1]
            if(distance[i[0]] > cost):
                distance[i[0]] = cost
                heapq.heappush(q, [i[0], cost])
               
dijkstra(X)

student = [0] * (N+1)
for i in range(1, N+1):
    if(distance[i] != INF):
        student[i] += distance[i]

dp = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
print(dp)
for i in range(1, N+1):
    if(distance[i] != INF):
        distance = [INF] * (N+1)
        dijkstra(i)
        if(distance[X] != INF):
            student[i] += distance[X]

print(max(student))