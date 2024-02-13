# https://www.acmicpc.net/problem/5719
import sys
import heapq
from collections import deque

input = sys.stdin.readline

INF = int(1e9) + 1

def disikstra():
    queue = []
    heapq.heappush(queue, (0 , S))
    distance[S] = 0
    
    while queue:
        dis, node = heapq.heappop(queue)
        
        if dis > distance[node]:
            continue
        
        for next_node in edge[node]:
            new_dis = cost[(node, next_node)] + dis
            if distance[next_node] > new_dis:
                distance[next_node] = new_dis
                heapq.heappush(queue, (new_dis, next_node))

def bfs():
    queue = deque([D])
    remove_node = list()
    while queue:
        node = queue.popleft()
        
        for next_node in r_edge[node]:
            if distance[next_node] == distance[node] - cost[(next_node, node)]:
                if (next_node, node) not in remove_node:
                    queue.append(next_node)
                    remove_node.append((next_node, node))

    return remove_node

while True:
    N, M = map(int, input().split())
    if N + M == 0:
        break
    
    S, D = map(int, input().split())
    edge = [set() for _ in range(N)]
    r_edge = [set() for _ in range(N)]
    cost = {}
    
    for _ in range(M):
        U, V, P = map(int, input().split())
        edge[U].add(V)
        r_edge[V].add(U)
        cost[(U, V)] = P
    
    distance = [INF for _ in range(N)]
    disikstra()
    remove_node = bfs()
    for cur, next in remove_node:
        edge[cur].discard(next)
    
    distance = [INF for _ in range(N)]
    disikstra()
    if distance[D] == INF:
        print(-1)
    else:
        print(distance[D])