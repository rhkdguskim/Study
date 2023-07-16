# https://www.acmicpc.net/problem/11727
N = int(input())
dp = [0 for _ in range(10001)]

dp[1] = 1
dp[2] = 3
dp[3] = 5

for i in range(4, len(dp)):
    dp[i] = dp[i-1] + 2 * dp[i-2]
    
print(dp[N] % 10007)