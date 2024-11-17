# https://www.acmicpc.net/problem/1520
import sys
input = sys.stdin.readline

sys.setrecursionlimit(501*501)

M, N = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1 for _ in range(N)] for _ in range(M)]

def dfs(y, x):
    if y == M-1 and x == N-1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0
    for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ny, nx = dy + y, dx + x
        if 0 <= ny < M and 0 <= nx < N and graph[y][x] > graph[ny][nx]:
            dp[y][x] += dfs(ny, nx)

    return dp[y][x]
        
print(dfs(0, 0))
