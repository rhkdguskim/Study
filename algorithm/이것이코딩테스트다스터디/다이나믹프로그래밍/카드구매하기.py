# https://www.acmicpc.net/problem/11052
N = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = arr[0]
for i in range(1, len(dp[0])):
    dp[0][i] = dp[0][i-1] + arr[0]
    
for i in range(1, N):
    for j in range(N):
        if j >= i:
            dp[i][j] = max(dp[i-1][j], dp[i][j-(i+1)] + arr[i])
        else:
            dp[i][j] = dp[i-1][j]
            
print(dp[N-1][N-1])