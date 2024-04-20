# https://www.acmicpc.net/problem/11657
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

edge = []
for _ in range(M):
    A, B, C = map(int, input().split())
    edge.append((A, B, C))
    
INF = int(1e15)

distance = [INF for _ in range(N+1)]
distance[1] = 0


def bellman_ford():
    is_cycle = False
    for i in range(N):
        for j in range(M):
            node1, node2, cost = edge[j]
            if distance[node1] != INF and distance[node2] > distance[node1] + cost:
                distance[node2] = distance[node1] + cost
                if i == N-1:
                    is_cycle = True
                    return is_cycle
    
    return is_cycle

if bellman_ford():
    print(-1)
else:
    for i in range(2, N+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])