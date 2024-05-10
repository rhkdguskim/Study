# https://school.programmers.co.kr/learn/courses/30/lessons/68937
# 3점이 모두 연결되어있고, 가장 멀리 떨어진 2개를 찾으면 된다.
# 트리...!!!!
# 모든 노드를 순회하면서 특정 노드에서 데이크스트라를 한뒤, 가장 멀리떨어진 노드 2개를 뽑아서 그중에
from itertools import combinations
from collections import deque
def solution(n, edges):
    distance = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    new_edge = [[] for _ in range(n+1)]
    for a, b in edges:
        new_edge[a].append(b)
        new_edge[b].append(a)
        
    def bfs(start, end):
        if distance[start][end] != -1:
            return distance[start][end]
        
        queue = deque()
        queue.append((start, 0))
        while queue:
            node, cost = queue.popleft()
            
            if node == end:
                distance[start][end] = cost
                distance[end][start] = cost
                return cost
            
            for child in new_edge[node]:
                new_cost = cost + 1
                queue.append((child, new_cost))
                
        return -1
    
    result = -1
    for a, b, c in combinations([i for i in range(1, n+1)], 3):
        answer = []
        answer.append(bfs(a, b))
        answer.append(bfs(b, c))
        answer.append(bfs(a, c))
        answer.sort()
        result = max(answer[1], result)

    return result