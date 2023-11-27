# https://www.acmicpc.net/problem/2293
import sys
input = sys.stdin.readline

n , k = map(int, input().split())
dp = [0 for _ in range(k+1)]
dp[0] = 1
coin = set()

for _ in range(n):
    coin.add(int(input()))

for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i-c]
        
print(dp[k])