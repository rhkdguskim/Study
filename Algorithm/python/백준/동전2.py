# https://www.acmicpc.net/problem/2294
# 동전의 개수가 최소면서, 가치의 합이 k원을 만들어라
INF = int(1e6)

from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

dp = [INF for _ in range(k+1)]

coin.sort(reverse=True)
queue = deque((num, 1) for num in coin)

while queue:
    num, cost = queue.popleft()
    
    if num > k:
        continue
    
    if num == k:
        dp[k] = cost
        break

    
    if dp[num] > cost:
        dp[num] = cost
        for new_coin in coin:
            queue.append((new_coin + num, cost + 1))
            
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])