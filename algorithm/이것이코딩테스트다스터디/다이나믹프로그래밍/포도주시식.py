# https://www.acmicpc.net/problem/2156
n = int(input())
item = []
for _ in range(n):
    item.append(int(input()))
if n > 2:
    dp = [0 for _ in range(n+1)]
    dp[0] = item[0]
    dp[1] = item[0]+item[1]
    dp[2] = max(dp[1], item[0]+item[2], item[1] + item[2])

    for i in range(3, n):
        dp[i] = max(dp[i-1], dp[i-2] + item[i], dp[i-3] + item[i] + item[i-1])

    print(dp[n-1])
else :
    if n == 1:
        print(item[0])
    if n == 2:
        print(item[0]+item[1])