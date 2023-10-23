# https://www.acmicpc.net/problem/2293
import sys
input = sys.stdin.readline

n , k = map(int, input().split())
dp = [0 for _ in range(k+1)]

coin = set()

for _ in range(n):
    coin.add(int(input()))

for c in coin:
    temp = [0 for _ in range(k+1)]
    for i in range(k+1):
        if i-c >= 0:
            temp[i] += dp[i-c]
        
        if i % c == 0:
            temp[i] += 1