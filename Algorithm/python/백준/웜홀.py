# https://www.acmicpc.net/problem/1865
# 벨만포드 알고리즘
# N * (M+W) 만큼 방문했을때 N-1 번째에서 갱신될경우 시간이 되돌아간다.

import sys
input = sys.stdin.readline

TC = int(input())


def bellman_ford(start):
    distance = [INF for _ in range(N+1)]
    distance[start] = 0
    for n in range(N):
        for e in range(M*2 + W):
            start, end, cost = edge[e][0], edge[e][1], edge[e][2]
            new_cost = distance[start] + cost
            if distance[end] > new_cost:
                distance[end] = new_cost
                
                if n == N-1:
                    return True
                
    return False
    
for _ in range(TC):
    N, M, W = map(int, input().split())
    
    edge = []
    INF = sys.maxsize
    
    for _ in range(M):
        S, E, T = map(int, input().split())
        edge.append((S, E, T))
        edge.append((E, S, T))
        
    for _ in range(W):
        S, E, T = map(int, input().split())
        edge.append((S, E, -T))
        
    if bellman_ford(1):
        print("YES")
    else:
        print("NO")