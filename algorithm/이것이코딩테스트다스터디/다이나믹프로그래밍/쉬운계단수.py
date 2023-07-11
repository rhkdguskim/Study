# https://www.acmicpc.net/problem/10844
N = int(input())
dp = [[0 for _ in range(11)] for _ in range(N+1)]

for i in range(1, len(dp[0]) -1):
    dp[1][i] = 1
    
for i in range(2, len(dp)):
    for j in range(0, len(dp[i]) -1):
        if j == 9:
            dp[i][j] = dp[i-1][j-1]
        elif j == 0:
            dp[i][j] = dp[i-1][j+1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(dp[N])
print(sum(dp[N]) % 1000000000)