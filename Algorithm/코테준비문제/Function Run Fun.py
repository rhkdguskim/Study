# https://www.acmicpc.net/problem/9184
import sys
input = sys.stdin.readline

dp = [[[-1 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def dfs(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return dfs(20, 20, 20)

    if dp[a][b][c] != -1:
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = dfs(a,b,c-1) + dfs(a, b-1, c-1) - dfs(a, b-1, c)
        return dp[a][b][c]

    cost = dfs(a - 1, b, c) + dfs(a - 1, b - 1, c) + dfs(a - 1, b, c - 1) - dfs(a - 1, b - 1, c - 1)
    dp[a][b][c] = cost
    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break

    print('w({}, {}, {}) = {}'.format(a, b, c, dfs(a,b,c)))




