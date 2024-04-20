# https://www.acmicpc.net/problem/15681
import sys
sys.setrecursionlimit(int(1e5) + 1)

input = sys.stdin.readline

N, R, Q = map(int, input().split())

dp = [-1 for _ in range(N+1)]
edge = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    edge[U].append(V)
    edge[V].append(U)

def dfs(parent):    
    
    dp[parent] = 1
    
    for child in edge[parent]:
        if dp[child] == -1:
            dp[parent] += dfs(child)
    
    return dp[parent]

dfs(R)

for _ in range(Q):
    query = int(input())
    print(dp[query])