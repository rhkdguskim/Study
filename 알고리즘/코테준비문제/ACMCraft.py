# https://www.acmicpc.net/problem/1005
import sys
input = sys.stdin.readline


def dfs(node):
    global ans
    for child in graph[node]:
        cost[child] -= 1 # 진입차수를 줄인다.
        ans[child] = max(ans[node] + distance[child], ans[child])

        if cost[child] == 0: # 진입차수가 0이면 이제 방문한다.
            dfs(child)

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    distance = [0] + list(map(int, input().split()))
    cost = [0 for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    ans = [0 for _ in range(N + 1)]

    for _ in range(K):
        X, Y = map(int, input().split())
        cost[Y] += 1 # 진입차수를 증가시킨다.
        graph[X].append(Y)

    rootnode = []
    for i in range(1, N+1): # 진입차수가 0인 노드부터 시작한다.
        if cost[i] == 0:
            rootnode.append(i)

    W = int(input())
    for node in rootnode:
        ans[node] = distance[node]
        dfs(node)
    print(ans[W])





