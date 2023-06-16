# https://www.acmicpc.net/problem/1504
N, M = map(int, input().split()) # N 정점의개수, M 간선의 개수
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
    
v1, v2 = map(int, input().split())

def dijkstra():