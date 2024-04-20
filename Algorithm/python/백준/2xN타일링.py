# https://www.acmicpc.net/problem/11726
# n이 1일때 1가지
# n이 2일때 2가지

# n이 3일때 dp[2]
# n이 4일때 dp[2] + 2, dp[1] * dp[3]

import sys
input = sys.stdin.readline
n = int(input())
dp = [0 for _ in range(n+1)]

if n >= 3:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n] % 10007)
else:
    if n == 1:
        print(1)
    else:
        print(2)