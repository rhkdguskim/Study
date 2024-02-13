# https://www.acmicpc.net/problem/1256
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

for i in range(1, M+1):
    dp[0][i] = 1
    
for i in range(1, N+1):
    dp[i][0] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

def dfs(a, z, cnt):
    if a == 0 or z == 0:
        if a == 0:
            return 'z'*z
        else:
            return 'a'*a
    
    if dp[a-1][z] >= cnt:
        return 'a' + dfs(a-1, z, cnt)
    else:
        return 'z' + dfs(a, z-1, cnt - dp[a-1][z])
    
if dp[N][M] >= K:
    print(dfs(N, M, K)) 
else:
    print(-1)

   