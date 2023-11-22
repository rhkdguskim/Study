# https://www.acmicpc.net/problem/2579
N = int(input())
stare = [0 for _ in range(N+1)]
dp = [[] for _ in range(N+1)]
for i in range(1, N+1):
    stare[i] = int(input())

if N >= 3:
    dp[1] = stare[1]
    dp[2] = stare[1] + stare[2]
    dp[3] = max(stare[1]+stare[3], stare[2]+stare[3])
    
    for i in range(4, N+1):
        dp[i] = max(dp[i-2]+stare[i], dp[i-3]+stare[i]+stare[i-1])
        
    print(dp[N])
else:
    print(sum(stare))
