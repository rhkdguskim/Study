# https://www.acmicpc.net/problem/1520
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1 for _ in range(N)] for _ in range(M)]
moves = [(0,1), (0,-1), (-1,0), (1,0)]
def dfs(i, j):
    #print(graph[i][j])
    if i == M-1 and j == N-1: # 도착했을때
        return 1
    
    if dp[i][j] != -1: # 이미 경로가 주어졌따면
        return dp[i][j]
    
    dp[i][j] = 0
    for dy, dx in moves:
        ny, nx = dy + i, dx + j
        if M > ny >= 0 and N > nx >=0 and graph[i][j] > graph[ny][nx]:
            dp[i][j] += dfs(ny, nx)
    
    return dp[i][j]

print(dfs(0,0))