#https://www.acmicpc.net/problem/2225
N , K = map(int, input().split())

dp = [[1 for _ in range(N+1) ] for _ in range(K)]

for i in range(1, K):
    for j in range(len(dp[i])):
        dp[i][j] = 0
        for k in range(j+1):
            dp[i][j] += dp[i-1][k]
            
        dp[i][j] = dp[i][j] % 1000000000
            
print(dp[K-1][N] % 1000000000)