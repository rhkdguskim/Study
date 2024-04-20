# https://www.acmicpc.net/problem/11404
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = 100001
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a, b , cost = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], cost)
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
for row in graph[1:]:
    for col in row[1:]:
        if col == INF:
            print(0, end = " ")
        else:
            print(col, end = " ")
    print()