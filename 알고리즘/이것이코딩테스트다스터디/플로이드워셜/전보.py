import heapq
INF = int(10e9)
N, M, C = map(int, input().split())
graph = [[] * (N+1)]

for _ in range(M):
    a, b ,c = map(int, input().split())
    graph[a].append([b, c])

distance = [INF] * (N+1)
def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, [start,0])
    while q:
       new, dis = heapq.heappop(q)
       if(distance[new] < dis):
           continue
       for i in graph[new]:
           cost = dis + i[1]
           if(cost < distance[i[0]]):
               distance[i[0]] = cost
               heapq.heappush(q, [i[0], cost])
               
dijkstra(C)
counter = 0
maxdata = 0
for data in distance:
    if(data != INF):
        counter+=1
        if(maxdata < data):
            maxdata = data
            
print(counter - 1, maxdata) # 시작노드는 제외해야함
