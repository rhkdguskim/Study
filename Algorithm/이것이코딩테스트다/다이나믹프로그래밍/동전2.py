# https://www.acmicpc.net/problem/2294
n, k = map(int, input().split())
coin = set()

for _ in range(n):
    coin.add(int(input()))
    
newcoin = sorted(coin)

INF = int(10e9)
dp = [INF for _ in range(k+1)]

for coin in newcoin:
    for i in range(1, len(dp)):
        if i % coin == 0:
            dp[i] = min(dp[i], i // coin)
        else:
            if i-coin > 0: # 인덱스 에러
                dp[i] = min(dp[i], dp[i-coin] + 1)
            
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])