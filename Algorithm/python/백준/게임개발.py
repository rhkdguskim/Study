import sys
input = sys.stdin.readline

N = int(input())

in_degree = [0 for _ in range(N)]
graph = []

for i in range(N):
    temp = list(map(int, input().split()))
    time = temp[0]
    temp = temp[1:-1]
    
    in_degree[i] += len(temp)
    graph.append((time, temp))

answer = []

def dfs(node, time):
    global answer
    for next in graph[node][1]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            dfs(next, time)