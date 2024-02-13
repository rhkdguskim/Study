#https://www.acmicpc.net/problem/1753
import heapq
# import sys 
# sys.setrecursionlimit(10**6)

V, E = map(int, input().split()) # 점점의 개수, 간선의 개수
INF = int(10e9)
graph = [[] for _ in range(V+1)]
start = int(input())
for _ in range(E):
    u, v, w = map(int, input().split()) # u에서 v로 가는 가중치 w
    graph[u].append([v,w])

    
    
dp = [INF for _ in range(V+1)]

def dfs(start, value):
    if dp[start] > value:
        dp[start] = value
        
        while graph[start]:
            v, w = graph[start].pop()
            dfs(v, value + w)
            
def dijkstra(start):
    queue = []
    dp[start] = 0
    heapq.heappush(queue, [0, start]) # 방문 거리를 최소힙 큐로 구현
    while queue:
        value , now = heapq.heappop(queue) # 가중치, 정점
        for u, v in graph[now]:# 정점, 가중치
            if dp[u] > value+v:
                dp[u] = value+v
                heapq.heappush(queue, [value+v, u])
        
#dfs(start,0)
dijkstra(start)

for i in range(1,len(dp)):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])