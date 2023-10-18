# https://www.acmicpc.net/problem/7579
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

dp = [[0 for _ in range(sum(C)+1)] for _ in range(N+1)]

ans = sum(C) + 1
for i in range(1, N+1):
    for j in range(1, sum(C)+1):
        if j >= C[i]: # 가중치가 더 클때만 넣을 수 있다.
            # 최대한 메모리를 크게 구해야 C의 가중치가 작게나온다.
            # 해당 앱이 있는경우와 없는경우
            dp[i][j] = max(dp[i-1][j-C[i]] + A[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

        if dp[i][j] >= M:
            ans = min(ans, j)

print(ans)