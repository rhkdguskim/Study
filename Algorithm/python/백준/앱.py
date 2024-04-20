# https://www.acmicpc.net/problem/7579
import sys
input = sys.stdin.readline
INF = int(1e10)

N, M = map(int, input().split())

m = list(map(int, input().split()))
c = list(map(int, input().split()))
dp = [[False for _ in range(100)] for _ in range(N)]

min_cost = INF
def dfs(idx, cost, memory):
    global min_cost
    if idx >= N or memory > M:
        return
    
    if dp[idx][cost]:
        return
    
    if memory == M:
        print(cost)
        min_cost = min(min_cost, cost)
        dp[idx][cost] = True
        return

    dfs(idx+1, cost+c[idx], memory+m[idx])
    dfs(idx+1, cost, memory)
    dp[idx][cost] = True
    return

dfs(0, 0, 0)
print(min_cost)
print(dp)