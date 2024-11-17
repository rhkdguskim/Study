# https://www.acmicpc.net/problem/2133
import sys
input = sys.stdin.readline

N = int(input())


dp=[0 for _ in range(N+2)]
dp[2]=3
for i in range(4,N+1):
    if i%2==0:
        dp[i]+=dp[i-2]*3
        for j in range(i-4,-1,-2):
            dp[i]+=2*dp[j]
        dp[i]+=2
        
print(dp[N])