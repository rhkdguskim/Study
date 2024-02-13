import heapq

N = int(input()) # 도시의 개수 (정점의 개수)
M = int(input()) # 버스의 개수 (간선의 개수)
INF = 10e9
graph = [[] for _ in range(N+1)] # 정점의 개수만큼 그래프를 생성한다.

for _ in range(M): # 그래프를 입력받는다
    a, b ,c = map(int, input().split()) # a : 출발도시, b: 도착도시 , c: 버스비용
    graph[a].append([b,c])

start , end = map(int, input().split()) # 출발도시, 도착도시

cost = [INF for _ in range(N+1)] # 정점의 최단경로 값

def dijkstra(start):
    q = []
    cost[start] = 0 # 자기자신에서 출발하면 비용은 0이다
    heapq.heappush(q, [0, start]) # 자기자신의 비용과 자기자신 인덱스번호를 최소힙에 Push한다.
    while q :
        buscost, now = heapq.heappop(q)
        if(cost[now] < buscost): # 이미 방문한곳이라면 스킵
            continue
        for i in graph[now]: # 방문할 노드 지정
            newcost = cost[now] + i[1]
            if(cost[i[0]] > newcost): # 최소비용이 발생할경우
                cost[i[0]] = newcost # 최소비용 업데이트
                heapq.heappush(q, [newcost, i[0]]) # 최소힙큐에 Push
                
dijkstra(start)
print(cost[end])