# https://www.acmicpc.net/problem/1956
import sys

V, E = map(int, input().split())
INF = sys.maxsize

edge = [[INF for _ in range(V+1)] for _ in range(V+1)]
distance = [[INF for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    edge[a][b] = c

for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j:
            distance[i][j] = 0
        else:
            distance[i][j] = edge[i][j]

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if distance[i][k] + distance[k][j] < distance[i][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

ans = INF
for i in range(1, V+1):
    for j in range(1, V+1):
        if i != j:
            ans = min(ans, distance[i][j] + distance[j][i])

if ans == INF:
    print(-1)
else:
    print(ans)
