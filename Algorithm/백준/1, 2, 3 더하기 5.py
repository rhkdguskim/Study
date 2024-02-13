# https://www.acmicpc.net/problem/15990
import sys
input = sys.stdin.readline
DIV = 1000000009
T = int(input())

dp = [[0 for _ in range(3)] for _ in range(100001)]
dp[1][0] = 1
dp[1][1] = 0
dp[1][2] = 0
dp[2][0] = 0
dp[2][1] = 1
dp[2][2] = 0
dp[3][0] = 1
dp[3][1] = 1
dp[3][2] = 1

for i in range(4, len(dp)):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % DIV
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % DIV
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % DIV
    
for _ in range(T):
    N = int(input())
    print(sum(dp[N]) % DIV)