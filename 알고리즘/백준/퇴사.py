# https://www.acmicpc.net/problem/15486
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1500001)

N = int(input())

t = []
p = []

for _ in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    
dp = [-1 for _ in range(N+1)]

def dfs(day, cost):
    if day >= N:
        if day == N:
            dp[day] = cost
            return dp[day]
        else:
            return 0
    
    if dp[day] != -1:
        return dp[day]
    
    if N >= day + t[day]:
        dp[day] = max(dp[day], dfs(day+t[day], cost + p[day]))
        
    dp[day] = max(dp[day], dfs(day + 1, cost))
    

    return dp[day]

print(dfs(0, 0))