# https://www.acmicpc.net/problem/1463
N = int(input())

dp = [0] * int(N+1)

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
        
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
        
    if i % 6 == 0:
        dp[i] = min(dp[i], dp[i//3]+1, dp[i//2]+1)
    
print(dp[N])