T = int(input())

def dfs(node, graph, d, dp):
    if dp[node] != -1:
        return dp[node]

    max_time = 0
    for prev_node in graph[node]:
        max_time = max(max_time, dfs(prev_node, graph, d, dp))

    dp[node] = max_time + d[node]
    return dp[node]

for _ in range(T):
    N, K = map(int, input().split())
    d = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    in_degree = [0] * (N + 1)
    
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y].append(X)
        in_degree[X] += 1
    
    W = int(input())
    dp = [-1] * (N + 1)
    end_nodes = [node for node in range(1, N + 1) if in_degree[node] == 0]
    
    for node in end_nodes:
        dfs(node, graph, d, dp)
    
    print(dp[W])