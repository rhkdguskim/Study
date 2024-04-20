import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N+2)]
prev = 0

for i in range(1, N+1):
    t, p = map(int, input().split())
    
    if dp[i] > prev:
        prev = dp[i]
        
    if N+1 >= i + t:
        dp[i+t] = max(dp[i+t], prev + p)

print(max(prev, dp[N+1]))