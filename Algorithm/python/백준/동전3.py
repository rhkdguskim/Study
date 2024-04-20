# https://www.acmicpc.net/problem/9084
import sys
input = sys.stdin.readline

result = []
for _ in range(int(input())):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())
    
    dp = [0 for _ in range(M+1)]
    dp[0] = 1
    
    for c in coin:
        for i in range(c, M+1):
            dp[i] += dp[i-c]
    
    print(dp[M])