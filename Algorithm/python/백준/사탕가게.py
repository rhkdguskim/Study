# https://www.acmicpc.net/problem/4781

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

INF = int(1e9)
def dfs(total):
    global ans
    if dp[total] != -1:
        return dp[total]
    
    temp = 0
    for c in candy:
        temp += dfs(total+c[0]) + c[1]
        if M >= temp:
            ans = max(total+c[0], ans)
    
    dp[total] = temp
    return dp[total]

while True:
    N , M = map(float, input().split())
    
    if N == 0:
        break
    candy = []
    total_cal = 0
    for i in range(int(N)):
        a, b = map(float, input().split())
        candy.append((int(a), b))
        total_cal += int(a)
    
    ans = 0
    dp = [-1 for _ in range(total_cal + 1)]
    dfs(0)
    print(ans)
    
