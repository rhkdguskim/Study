#https://www.acmicpc.net/problem/11066
T = int(input())
for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]
    for j in range(1, K):
        for i in range(j-1, -1 , -1):
            minvalue = int(10e9)
            for k in range(j-i):
                minvalue = min(minvalue, dp[i][i+k] + dp[i+k+1][j])
            
            dp[i][j] = minvalue + sum(arr[i:j+1])
            
                    

    print(dp[0][K-1])
    
    