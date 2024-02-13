# https://www.acmicpc.net/problem/2748
n = int(input())
dp = [0 for _ in range(91)]

dp[0] = 0
dp[1] = 1
for i in range(2,len(dp)):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])