# https://school.programmers.co.kr/learn/courses/30/lessons/67260

from collections import deque, defaultdict

def solution(n, path, order):
    graph = defaultdict(list)
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)
    
    pre_visit = [-1] * n
    post_visit = [-1] * n
    
    for a, b in order:
        pre_visit[b] = a
    
    if pre_visit[0] != -1:
        return False
    
    visited = [False] * n
    q = deque([0])
    visited[0] = True
    
    while q:
        node = q.popleft()
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                # 선행 방문 노드가 있는 경우, 아직 선행 노드를 방문하지 않았다면
                if pre_visit[neighbor] != -1 and not visited[pre_visit[neighbor]]:
                    # 추후 방문 노드로 설정해준다.
                    post_visit[pre_visit[neighbor]] = neighbor
                    continue
                
                # 방문 처리
                visited[neighbor] = True
                q.append(neighbor)
                
                # 후행 방문 노드가 대기 중인 경우
                if post_visit[neighbor] != -1:
                    next_node = post_visit[neighbor]
                    visited[next_node] = True
                    q.append(next_node)
    
    return all(visited)