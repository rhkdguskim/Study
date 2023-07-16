import heapq
import sys
input = sys.stdin.readline()
INF = 10e9

#노드개수, 간선개수 입력받기
n, m = map(int,input().split())
# 시작 노드 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)]
# 최단거리 테이블 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for i in range(m):
    a, b, c = map(int, input().split()) # a : 노드 , b: 연결된노드 , c : 간선길이
    graph[a] = [b, c]

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start)) 
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist , now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if (distance[now] < dist):
            continue
        # 현재 노드와 연결된 다른 입접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            if(distance[i[0]] > cost):
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF :
        print("도달 할 수 없음")
    else :
        print(distance[i])
