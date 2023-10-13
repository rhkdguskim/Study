# https://www.acmicpc.net/problem/10942
import sys
sys.setrecursionlimit(20000000)

N = int(input())
arr = list(map(int ,input().split()))
M = int(input())


dp = [[0 for _ in range(N)] for _ in range(N)]

def dfs(start, end):
    if 0 > start and end > N:
        return 0

    if start > end:
        return 0
    else:
        left = start
        right = end
        if left == right: # 자기자신은 팰린드롬이다
            dp[left][right] = 1
            return 1
        else:
            if arr[left] == arr[right]: # 만약 팰린드롬이라면
                dp[left][right] = dfs(start +1, end -1) # +1, -1 재귀로 했을때
            else:
                dp[left][right] = 0
                
            dp[left][right-1] = dfs(start, end-1)
            dp[left+1][right] = dfs(start+1, end)
            
    return dp[left][right]
    
dfs(0, N-1)
    
for _ in range(M):
    left, right = map(int, input().split())
    print(dp[left-1][right-1])
    

    