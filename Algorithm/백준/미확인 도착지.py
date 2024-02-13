import sys

from heapq import heappop, heappush
INF = int(1e9)

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    edge = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b, d = map(int, input().split())
        edge[a].append((b, d))
        edge[b].append((a, d))
    
    destination = set(int(input()) for _ in range(t))
    distance = [INF for _ in range(n+1)]
    
    queue = []
    heappush(queue, (0, s, False))
    
    result = set()
    
    while queue:
        cost, node, is_meet = heappop(queue)
        
        if cost > distance[node]:
            continue
        
        distance[node] = cost
        if node in destination:
            if is_meet:
                result.add(node)
        
        for new_node, new_cost in edge[node]:
            
            if distance[new_node] > new_cost + cost:
                if (node == h and new_node == g) or (node == g and new_node == h):
                    heappush(queue, (new_cost + cost, new_node, True))
                else:
                    heappush(queue, (new_cost + cost, new_node, is_meet))
                
    result = list(result)
    result.sort()
    print(' '.join(map(str, result)))
    