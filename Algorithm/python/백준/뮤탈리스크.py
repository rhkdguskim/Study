# https://www.acmicpc.net/problem/12869
# 9 3 1
import sys
input = sys.stdin.readline
INF = int(10e9)
N = int(input())
temp = list(map(int, input().split()))
scv = [0 for _ in range(3)]
for i in range(N):
    scv[i] = temp[i]
    
dp = [[[INF for _ in range(61)] for _ in range(61)] for _ in range(61)]
def dfs(cnt, scv1, scv2, scv3):
    if scv1 <=0 and scv2 <=0 and scv3<=0:
        return cnt
    
    # 음스의 경우는 0으로 초기화 해준다.
    scv1 = max(0, scv1)
    scv2 = max(0, scv2)
    scv3 = max(0, scv3)
    
    if dp[scv1][scv2][scv3] != INF:
        return dp[scv1][scv2][scv3]
    
    # scv1 부터 때린다.
    if scv1 > 0:
        dp[scv1][scv2][scv3] = min(dfs(cnt +1, scv1 - 9, scv2 - 3, scv3 - 1), dp[scv1][scv2][scv3])
        dp[scv1][scv2][scv3] = min(dfs(cnt +1, scv1 - 9, scv2 - 1, scv3 - 3), dp[scv1][scv2][scv3])
        
    if scv2 > 0:
        dp[scv1][scv2][scv3] = min(dfs(cnt +1, scv1 - 3, scv2 - 9, scv3 - 1), dp[scv1][scv2][scv3])
        dp[scv1][scv2][scv3] = min(dfs(cnt +1, scv1 - 1, scv2 - 9, scv3 - 3), dp[scv1][scv2][scv3])
    
    if scv3 > 0:
        dp[scv1][scv2][scv3] = min(dfs(cnt +1, scv1 - 1, scv2 - 3, scv3 - 9), dp[scv1][scv2][scv3])
        dp[scv1][scv2][scv3] = min(dfs(cnt +1, scv1 - 3, scv2 - 1, scv3 - 9), dp[scv1][scv2][scv3])
    
    return dp[scv1][scv2][scv3]

print(dfs(0, scv[0], scv[1], scv[2]))
    