# https://www.acmicpc.net/problem/11049
import sys
input = sys.stdin.readline

N = int(input())
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
for i in range(N):
    r, c = map(int, input().split())
    dp[i][i] = [r, c, 0]

for i in range(N-1):
    temp = dp[i][i][0] * dp[i+1][i+1][0] * dp[i+1][i+1][1]
    dp[i][i+1] = [dp[i][i][0], dp[i+1][i+1][1], temp]

for i in range(2, N):
    for j in range(N-i):
        # 나중에 계산한 결과 (AB)(C)
        temp1 = dp[j][i+j-1][2] + dp[j][i+j-1][0] * dp[i+j][i+j][0] * dp[i+j][i+j][1]
        # 먼저 계산한 결과 (A)(BC)
        temp2 = dp[j][j][0] * dp[j+1][i+j][0] * dp[j+1][i+j][1] + dp[j+1][i+j][2]

        if temp2 > temp1: # 작은 친구를 선택한다.
            dp[j][i+j] = [dp[j][i+j-1][0], dp[i+j][i+j][1], temp1]
        else:
            dp[j][i+j] = [dp[j][j][0], dp[j+1][i+j][1], temp2]

print(dp[0][N-1][2])