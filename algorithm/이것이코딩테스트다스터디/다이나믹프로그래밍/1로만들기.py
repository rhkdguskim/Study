X = int(input())
counter = 0
dp = [0] * 30001
dp[0] = 1
i = 0
while(dp[i] != X):
    if(X >= max(dp[i]*5, dp[i]*3, dp[i]*2, dp[i] + 1)):
        dp[i+1] = max(dp[i]*5, dp[i]*3, dp[i]*2, dp[i] + 1)
    elif (X >= max(dp[i]*3, dp[i]*2, dp[i] + 1)):
        dp[i+1] = max(dp[i]*3, dp[i]*2, dp[i] + 1)
    elif (X >= max(dp[i]*2, dp[i] + 1)):
        dp[i+1] = max(dp[i]*2, dp[i] + 1)
    else :
        dp[i+1] = dp[i] + 1

    i += 1
    
print(i)

