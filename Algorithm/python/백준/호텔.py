# https://www.acmicpc.net/problem/1106
import sys
input = sys.stdin.readline
INF = int(1e9)

C, N = map(int, input().split())
info = []

for _ in range(N):
    c, n = map(int, input().split())
    info.append((c, n))

# 명수가 가장 크면서, 비용이 작은것부터 채운다.
info.sort(key=lambda x:(-x[1], x[0]))
dp = [INF for _ in range(2001)]
dp[0] = 0

for c, n in info:
    i = 1
    while 2000 >= i:
        if i - n >= 0:
            dp[i] = min(dp[i], dp[i - n] + c)
        i += 1


print(min(dp[C:]))
#print(dp)