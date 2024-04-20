# https://school.programmers.co.kr/learn/courses/30/lessons/92343
# BFS로 양을 먼저 방문한다. 우선순위 큐
# 양은 무조건 먼저 방문한다. (0)
# 늑대인데 리프노드인경우는 가지 않는다.
# 늑대인데 자식으로 양이 2마리 있는경우 (1), 1마리 있는경우(2), 늑대 1마리 있는경우(3), 늑대 2마리 있는경우(4) 순으로 먼저 방문해야한다.
import heapq

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        a, b = edge[:]
        graph[a].append(b)
    
    
    queue = []
    sheep = 0
    wolf = 0
    # 루트노드로 부터 시작
    queue.append((0, 0))
    
    while queue:
        _, n_node = heapq.heappop(queue)
        print("node : ", n_node)
        if info[n_node] == 0: # 양인경우
            sheep += 1
        else:
            wolf += 1
            
        if sheep == wolf:
            break
        
        for n2_node in graph[n_node]:
            if info[n2_node] == 0: # 양인경우
                heapq.heappush(queue, (-3, n2_node))
            else:
                # 늑대인경우 리프노드가 아닌경우 방문한다.
                if graph[n2_node]:
                    n_cost = 0
                    for n3_node in graph[n2_node]:
                        if info[n3_node] == 0: # 자식이 양 인 경우
                            n_cost -= 1
                        else: # 자식이 늑대인경우
                            n_cost += 1
                    heapq.heappush(queue, (n_cost, n2_node))
        
    
    
    return sheep

# info = [0,0,1,1,1,0,1,0,1,0,1,1]
# edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))