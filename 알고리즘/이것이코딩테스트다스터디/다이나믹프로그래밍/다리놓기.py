# https://www.acmicpc.net/problem/1010

T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    dp = [[0 for _ in range(N+1)] for _ in range(M+1)]
    for i in range(N+1):
        dp[i][i] = i
    
    for i in range(M+1):
        dp[i][1] = i
        
    for i in range(2, M+1):
        for j in range(2,N+1):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            
    print(dp[M][N])