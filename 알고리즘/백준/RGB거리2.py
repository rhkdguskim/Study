# https://www.acmicpc.net/problem/17404
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]

ans = INF
for i in range(3):
    dp = [[INF for _ in range(3)] for _ in range(N)]
    dp[0][i] = home[0][i]
    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + home[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + home[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + home[j][2]
    
    
    for k in range(3):
        if i != k:
            ans = min(ans, dp[-1][k])
    
print(ans)