import heapq
N, M, K, X = map(int, input().split()) # N 도시의 개수 M 도로의 개수, K 거리 정보, 출발도시 번호 X
INF = int(10e9)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a , b = map(int, input().split())
    graph[a].append(b)
    
distance = [INF] * (N+1)

def dijksta(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (distance[start], start))
    
    while queue:
        dis, now = heapq.heappop(queue)
        if distance[now] < dis:
            continue
        
        for idx in graph[now]:
            cost = distance[now] + 1
            if distance[idx] > cost:
                distance[idx] = cost
                heapq.heappush(queue ,(distance[idx], idx))

dijksta(X)
arr = []
for i in range(len(distance)):
    if(distance[i] != INF and distance[i] == K):
        arr.append(i)

arr.sort()
if len(arr) == 0:
    print(-1)
else :
    for idx in arr: 
        print(idx)