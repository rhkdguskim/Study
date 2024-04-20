# https://www.acmicpc.net/problem/2240
import sys
input = sys.stdin.readline

T, W = map(int, input().split())
jadu = [int(input()) for _ in range(T)]
dp = [[0 for _ in range(W+1)] for _ in range(T)]

for i in range(T):
    if jadu[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]
    for j in range(1, W+1):
        if j % 2 == 1 and jadu[i] == 2:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        elif j % 2 == 0 and jadu[i] == 1:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[T-1]))
        