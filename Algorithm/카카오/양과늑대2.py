def dfs(visited : list, sheep, wolf, graph, info):
    if wolf >= sheep:
        #print(visited, sheep, wolf)
        return sheep
    
    result = -1
    for node in visited:
        for new_node in graph[node]:
            if new_node not in visited:
                visited.append(new_node)
                if info[new_node] == 0:
                    result = max(result, dfs(visited, sheep+1, wolf, graph, info))
                else:
                    result = max(result, dfs(visited, sheep, wolf+1, graph, info))
                    
                visited.pop()
            
    return result
                
def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        a, b = edge[:]
        graph[a].append(b)

    return dfs([0], 1, 0, graph, info)

    
info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

# info = [0,1,0,1,1,0,1,0,0,1,0]
# edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))


def solution(info, edges):
    visited = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                visited[c] = 0

	# 루트 노드부터 시작
    visited[0] = 1
    dfs(1, 0)

    return max(answer)