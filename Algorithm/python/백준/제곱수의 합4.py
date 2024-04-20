# https://www.acmicpc.net/problem/1699
import sys
from math import sqrt
input = sys.stdin.readline
INF  = float('inf')
N = int(input())
sys.setrecursionlimit(int(1e5))

dp = [INF for _ in range(N+1)]

def is_squre(number):
    sqrt_n = sqrt(number)
    return sqrt_n == int(sqrt_n)

def dfs(number):
    if number == 0:
        return 0
    
    if is_squre(number):
        dp[number] = 1
        return 1
    
    if dp[number] != INF:
        return dp[number]
    
    for i in range(int(number ** 0.5), 0, -1):
        squre = i*i
        
        if squre > number:
            break
        
        dp[number] = min(dp[number], dfs(number - squre) + 1)
        
    return dp[number]

print(dfs(N))