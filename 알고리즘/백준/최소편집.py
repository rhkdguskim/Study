# https://www.acmicpc.net/problem/15483
import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

s_len = len(S)
t_len = len(T)
dp = [[0 for _ in range(t_len+1)] for _ in range(s_len+1)]

for i in range(s_len+1):
    dp[i][0] = i

for i in range(t_len+1):
    dp[0][i] = i

for i in range(1, s_len+1):
    for j in range(1, t_len+1):
        if S[i-1] == T[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

print(dp[s_len][t_len])