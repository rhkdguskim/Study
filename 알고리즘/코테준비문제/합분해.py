# https://www.acmicpc.net/problem/2225
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

dp[0][1] = 2

for i in range(1, N+1):
    for j in range(i-1, -1, -1):
        for k in range(K, 0, -1):
            dp[i][k] += dp[j][k-1]

print(dp[N][K])