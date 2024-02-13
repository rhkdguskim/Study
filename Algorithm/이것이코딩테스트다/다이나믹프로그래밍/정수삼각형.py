# https://www.acmicpc.net/problem/1932
N = int(input())

triangle = []
dp = [[0 for _ in range(N+1)] for _ in range(N)]
for _ in range(N):
    arr = list(map(int, input().split()))
    triangle.append(arr)
    
dp[0][0] = triangle[0][0]
for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
print(max(dp[N-1]))