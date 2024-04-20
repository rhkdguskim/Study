# https://www.acmicpc.net/problem/2169
import sys
INF = -int(1e10)
input = sys.stdin.readline

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

dp = [[INF for _ in range(M)] for _ in range(N)]
dp[0][0] = table[0][0]

for i in range(1, M):
    dp[0][i] = dp[0][i-1] + table[0][i]

for i in range(1, N):
    left = [0 for _ in range(M)]
    left[0] = table[i][0] + dp[i-1][0]
    
    right = [0 for _ in range(M)]
    right[M-1] = table[i][M-1] + dp[i-1][M-1]
    for j in range(1, M):
        left[j] = max(left[j-1] + table[i][j], dp[i-1][j] + table[i][j])
        right[M-j-1] = max(right[M-j] + table[i][M-j-1], dp[i-1][M-j-1] + table[i][M-j-1])
    
    for k in range(M):
        dp[i][k] = max(left[k], right[k])    

print(dp[N-1][M-1])
            