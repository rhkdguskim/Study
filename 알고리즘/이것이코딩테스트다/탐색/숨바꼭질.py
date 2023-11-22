# https://www.acmicpc.net/problem/13549
INF = int(10e9)
N, K = map(int, input().split())

dp = [INF for _ in range(100000+1)] # dp 테이블을 무한대 값으로 초기화한다.

for i in range(0, N+1):
    dp[i] = abs(N - i)
    

for i in range(N+1, K+1):
    if i % 2 == 0: # 짝수이면
        if i != K:
            dp[i] = min(dp[i//2], dp[i-1]+1, dp[i+1]+1)
        else:
            dp[i] = min(dp[i//2], dp[i-1]+1)
    else : # 홀수이면
        if i != K:
            dp[i] = min(dp[i-1]+1, dp[i+1]+1, dp[i//2]+1)
        else:
            dp[i] = min(dp[i-1]+1, dp[i//2]+1)

print(dp[K]) # 동생까지의 최단경로를 구한다.