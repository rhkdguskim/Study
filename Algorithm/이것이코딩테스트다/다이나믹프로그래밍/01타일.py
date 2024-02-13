# https://www.acmicpc.net/problem/1904
N = int(input())

if N > 3:
    dp = [0 for _ in range(N+1)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    for i in range(4,N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
        
    print(dp[N])
else:
    print(N)