import heapq
INF = int(10e9)
test = int(input())

def dijkstra(start, distance, graph):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (distance[start], start))
    while queue:
        dis, now = heapq.heappop(queue)
        if(distance[now] < dis):
            continue
        
        for i in graph[now]:
            cost = distance[now] + i[0]
            if distance[i[1]] > cost:
                distance[i[1]] = cost
                heapq.heappush(queue, (cost, i[1]))
    
    
for _ in range(test):
    n, d, c = map(int, input().split()) # n 컴퓨터개수, d 의존성개수, c 해킹당한 컴퓨터
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for _ in range(d):
        com1, com2, time = map(int, input().split())
        graph[com2].append([time, com1])
    dijkstra(c, distance, graph)
    hackedcom = []
    for i in range(len(distance)):
        if(distance[i] != INF):
            hackedcom.append(distance[i])
            
    print(len(hackedcom), end=' ') # 감염되는 총 컴퓨터수
    print(max(hackedcom)) # 마지막 컴퓨터가 감염되기까지 걸리는 시간