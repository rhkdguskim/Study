# https://www.acmicpc.net/problem/11057
N = int(input())

dp = [1 for _ in range(10)]

for _ in range(N-1):
    for i in range(len(dp)):
        for j in range(i+1, len(dp)):
            dp[i] += dp[j]

print(sum(dp) % 10007)