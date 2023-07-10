# https://www.acmicpc.net/problem/10844
N = int(input())
dp = [0 for _ in range(N+1)]
dp[1] = 9
dp[2] = 17

for i in range(3, N+1):
    dp[i] = 2*(dp[i-1]) -1

if N == 1:
    print(1)
else:
    print(dp[N] % 1000000000)