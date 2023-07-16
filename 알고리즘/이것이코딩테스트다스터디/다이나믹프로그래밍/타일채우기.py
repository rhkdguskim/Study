# https://www.acmicpc.net/problem/2133
N = int(input())
dp = [0 for _ in range(N+1)]
if N > 3:
    dp[0] = 1
    dp[1] = 0
    dp[2] = 3
    dp[3] = 0
    for i in range(4, len(dp)):
        if i % 4 == 0:
            dp[i] = dp[i-2]*3 + dp[i-4]*2
        else:
            dp[i] = dp[i-2]*3
            
    print(dp[N])
else:
    if N == 1 or N == 3:
        print(0)
    else:
        print(3)