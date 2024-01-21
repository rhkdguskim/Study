# https://www.acmicpc.net/problem/2240
import sys
input = sys.stdin.readline

T, W = map(int, input().split())
jadu = [int(input()) for _ in range(T)]
dp = [[-1 for _ in range(W+1)] for _ in range(T)]

def dfs(index, cnt):
    if index >= T:
        return 0
    
    if dp[index][cnt] != -1:
        return dp[index][cnt]
    
    eat_value = 0
    if cnt % 2 == 1 and jadu[index] == 2: # 2에 있는경우
        eat_value = 1
    
    if cnt % 2 == 0 and jadu[index] == 1: # 1에 있는경우
        eat_value = 1
    
    dp[index][cnt] = max(dp[index][cnt], dfs(index+1, cnt) + eat_value)
        
    if W >= cnt + 1:
        dp[index][cnt] = max(dp[index][cnt], dfs(index+1, cnt + 1) + eat_value)
        
    return dp[index][cnt]

print(max(dfs(0, 0), dfs(0, 1)))