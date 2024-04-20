# https://www.acmicpc.net/problem/7579
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

m = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
sum_c = sum(c)

dp = [[0 for _ in range(sum_c+1)] for _ in range(N+1)]

min_result = 10001
for i in range(1, N+1):
    for j in range(1, sum_c+1):
        if j >= c[i]:
            dp[i][j] = max(dp[i-1][j-c[i]]+m[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
        
        if dp[i][j] >= M:
            min_result = min(min_result, j)
            
if M == 0:
    print(0)
else:
    print(min_result)