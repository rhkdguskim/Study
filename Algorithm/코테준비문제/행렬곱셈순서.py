# https://www.acmicpc.net/problem/11049
# ABCD
# (ABC)(D)
# (AB)(CD)
# (A)(BCD)
# ABCDE
# (A)(BCDE)
# (AB)(CDE)
# (ABC)(DE)
# (ABCD)(E)
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
        mincost = int(2**31)
        for k in range(i):
            r1, c1, cost1 = dp[j][j+k][0], dp[j][j+k][1], dp[j][j+k][2]
            r2, c2, cost2 = dp[j+k+1][i+j][0], dp[j+k+1][i+j][1], dp[j+k+1][i+j][2]

            temp = cost1 + cost2 + (r1 * c1 * c2)
            if mincost > temp:
                mincost = temp
                n_r1 = r1
                n_c1 = c2

        dp[j][j+i] = [n_r1, n_c1, mincost]

print(dp[0][N-1][2])