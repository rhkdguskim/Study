# https://school.programmers.co.kr/learn/courses/30/lessons/118669
# 출발지로부터 쉼터까지 intensity
# 쉼터로부터 산봉우리까지 intensity


# 쉼터부터 산봉우리까지의 최단경로인 intensity를 구한다. (거리와 노드)

def solution(n, paths, gates, summits): # 출발지, 산봉우리
    answer = []
    return answer

def update_break_to_summits(n, path, gates, summits):
    source = [i for i in range(1, n) if i not in gates and i not in summits]
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i, j, w in path:
        graph[i] = (w, j) # 거리, 타깃
        graph[j] = (w, i)
    
    