# https://www.acmicpc.net/problem/1699
import sys
input = sys.stdin.readline

N = int(input())

dp = [i for i in range(N+1)]

for i in range(2, N+1):
    for j in range(1, i+1):
        squre = j*j
        if squre > i:
            break
        
        dp[i] = min(dp[i], dp[i-squre]+1)

print(dp[N])