# https://school.programmers.co.kr/learn/courses/30/lessons/72413

# 데이크스트라를 한뒤 역추적한다.
# a와 b로 가는 경로를 거꾸로 역추적 한다.
# a와 b의 공통 길을 한번 빼준다.
import sys
import heapq

def solution(n, s, a, b, fares):
    # 거리 테이블 초기화
    distance = [sys.maxsize] * (n+1)
    
    edge =[[] for _ in range(n+1)]
    
    for c, d, f in fares:
        edge[c].append((d, f))
        edge[d].append((c, f))
    
    queue = []
    heapq.heappush(queue, (0, s))
    distance[s] = 0
    
    while queue:
        cost, node = heapq.heappop(queue)

        if cost > distance[node]:
            continue
        
        distance[node] = cost
        
        for next, next_cost in edge[node]:
            new_cost = next_cost + cost
            if distance[next] > new_cost:
                distance[next] = new_cost
                queue.append((new_cost, next))
        
        
    path_a = []
    cur_node = a
    while cur_node != s:
        
        for next, cost in edge[cur_node]:
            if distance[cur_node] - cost == distance[next]:
                cur_node = next
                path_a.append(next)
                break
    
    path_b = []
    cur_node = b
    while cur_node != s:
        for next, cost in edge[cur_node]:
            if distance[cur_node] - cost == distance[next]:
                cur_node = next
                path_b.append(next)
                break
            
    print(path_a)
    print(path_b)
    return 0

solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])