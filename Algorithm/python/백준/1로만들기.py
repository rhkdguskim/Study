import sys
input = sys.stdin.readline
INF = int(1e9)

X = int(input())

dp = [INF for _ in range(X+1)]
dp[1] = 0

for i in range(1, X+1):
    if X >= i*5: # 5를 곱한다.
        dp[i*5] = min(dp[i] + 1, dp[i*5])
    
    if X >= i*3:
        dp[i*3] = min(dp[i] + 1, dp[i*3])
        
    if X >= i*2:
        dp[i*2] = min(dp[i] + 1, dp[i*2])
        
    if X >= i+1:
        dp[i+1] = min(dp[i] + 1, dp[i+1])
        
print(dp[X])