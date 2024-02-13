INF = int(10e9)

N, M = map(int, input().split()) # N : 회사의개수(정점의개수), M 경로의개수(간선의개수)
graph = [[INF]*(N+1) for _ in range(N+1)] # 각 값이 INF인 2차원 배열 생성

for i in range(N+1):
    graph[i][i] = 0
    
for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
X, K = map(int, input().split())
    
for i in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])
            
print(graph[1][K] + graph[K][X])