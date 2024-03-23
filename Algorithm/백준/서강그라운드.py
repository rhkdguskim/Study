# https://www.acmicpc.net/problem/14938
# 플로이드 워셜

import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())

items = list(map(int, input().split()))
INF = sys.maxsize
distance = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    distance[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    distance[a][b] = l
    distance[b][a] = l
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])

ans = 0
for i in range(1, n+1):
    count = items[i-1]
    for j in range(1, n+1):
        if i != j:
            if m >= distance[i][j]:
                count += items[j-1]
    ans = max(count, ans)
    
print(ans)