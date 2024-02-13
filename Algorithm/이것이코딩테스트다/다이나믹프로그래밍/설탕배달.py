# https://www.acmicpc.net/problem/2839
N = int(input())
dp = [5001] * int(5000+1)
dp[3] = 1
dp[5] = 1

for i in range(6, N+1):
    dp[i] = min(dp[i-3], dp[i-5]) + 1

if dp[N] >= 5001:
    print(-1)
else:
    print(dp[N])