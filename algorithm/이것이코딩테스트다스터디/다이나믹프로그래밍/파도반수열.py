# https://www.acmicpc.net/problem/9461
T = int(input())
INF = int(10e9)
dp = [0 for _ in range(101)]
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3

for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]
    
for _ in range(T):
    number = int(input())
    print(dp[number])