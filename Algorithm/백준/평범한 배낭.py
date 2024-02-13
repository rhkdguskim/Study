# https://www.acmicpc.net/problem/12865
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

value = []
weight = []
for _ in range(N):
    W, V = map(int, input().split())
    value.append(V)
    weight.append(W)
    
dp = [[-1 for _ in range(K+1)] for _ in range(N)]
def dfs(idx, w):
    if idx >= N:
        return 0
    
    if dp[idx][w] != -1:
        return dp[idx][w]
    
    dp[idx][w] = max(dp[idx][w], dfs(idx+1, w))
    
    if K >= w + weight[idx]:
        dp[idx][w] = max(dp[idx][w], dfs(idx+1, w + weight[idx]) + value[idx])
        
    return dp[idx][w]      
    
print(dfs(0, 0))