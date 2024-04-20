# https://www.acmicpc.net/problem/2133
N = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
dp[4] = 3*3 + 2
for i in range(5, len(dp)):
    if i % 2 == 0:
        dp[i] = dp[i-2] * 3 + dp[i-4] * 2

print(dp[N])