#https://www.acmicpc.net/problem/9465
T = int(input())

for _ in range(T):
    n = int(input())
    dp = [[0 for _ in range(2)] for _ in range(n)]
    uparr = list(map(int, input().split()))
    downarr = list(map(int, input().split()))
    if n == 1:
        print(max(uparr[0], downarr[0]))
    elif n == 2:
        print(max(downarr[0] + uparr[1], uparr[0] + downarr[1]))
    else:
        dp[0][0] = uparr[0]
        dp[0][1] = downarr[0]
        dp[1][0] = downarr[0] + uparr[1]
        dp[1][1] = uparr[0] + downarr[1]
        for i in range(2, n):
            for j in range(2):
                if j == 0:
                    dp[i][j] = max(dp[i-1][1], dp[i-2][1], dp[i-2][0]) + uparr[i]
                else:
                    dp[i][j] = max(dp[i-1][0], dp[i-2][0], dp[i-2][1]) + downarr[i]

        print(max(dp[n-1][0],dp[n-1][1]))