# https://school.programmers.co.kr/learn/courses/30/lessons/68937

from collections import deque
def solution(n, edges):
    new_edge = [[] for _ in range(n+1)]
    for a, b in edges:
        new_edge[a].append(b)
        new_edge[b].append(a)
        
    def bfs(start):
        distance = []
        queue = deque()
        queue.append((start, 0))
        visited = {start : 1}
        
        while queue:
            node, cost = queue.popleft()
            distance.append((node, cost))
            
            for child in new_edge[node]:
                if child not in visited:
                    visited[child] = 1
                    new_cost = cost + 1
                    queue.append((child, new_cost))

        return distance
    
    check = bfs(1)
    end = bfs(check[-1][0])
    if check[-1][1] == check[-2][1]:
        return end[-1][1]
    else:
        return end[-2][1]