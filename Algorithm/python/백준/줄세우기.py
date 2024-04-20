# https://www.acmicpc.net/problem/2631
import sys
input = sys.stdin.readline

N = int(input())
child = [int(input()) for _ in range(N)]
dp = [[int(1e5) for _ in range(N)] for _ in range(N)]

for i in range(N-1):
    if child[i] > child[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0

for j in range(2, N):
    for i in range(N-j):
        left_max = max(child[i:j+i])
        right_min = min(child[i+1:j+i+1])
        left_cost = 0
        right_cost = 0
        if left_max > child[j+i]:
            left_cost = 1
            
        if right_min > child[i]:
            right_cost = 1
            
        dp[i][j+i] = min(dp[i][j+i-1] + left_cost, dp[i+1][j+i] + right_cost)
        print(dp[i][j+i], i, j+i)
        

print(dp[0][N-1])
for d in dp:
    print(d)
# (0, 2) => (0, 1) arr[2],  arr[1], (1, 2) 
# (1, 3) => (1, 2) arr[3], arr[1], (2, 3)
# (2, 4) =>
# (i, i+k) => (i, i+k-1), (i+1, i+k)

# (0, 3)
# (1, 4)
# (2, 5)