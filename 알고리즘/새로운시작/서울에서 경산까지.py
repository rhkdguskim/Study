# https://www.acmicpc.net/problem/14863
# 배낭문제와 유형이 똑같다.
# 걸리는 시간을 가방에 넣을 수 있는 최대 무게라고 생각하면 된다.
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 0번째 idx는 Dummy 값이다.

walk = [(0,0)]
bike = [(0,0)]
for _ in range(N):
    a, b, c , d = map(int, input().split())
    walk.append((a, b)) # 시간, 모금액
    bike.append((c, d)) # 시간, 모금액
    
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
ans = 0
dp[1][walk[1][0]] = max(dp[1][walk[1][0]], walk[1][1])
dp[1][bike[1][0]] = max(dp[1][bike[1][0]], bike[1][1])

for i in range(2, N+1):
    for j in range(K+1):
        if dp[i-1][j] != 0:
            # 걸어서 가는경우
            if j + walk[i][0] <= K:
                dp[i][j+walk[i][0]] = max(dp[i][j+walk[i][0]], dp[i-1][j] + walk[i][1])
                
            # 자전거를 타고 가는경우
            if j + bike[i][0] <= K:
                dp[i][j+bike[i][0]] = max(dp[i][j+bike[i][0]], dp[i-1][j] + bike[i][1])
                

# 마지막에 지역에 도달했을때의 최대값
for j in range(K+1):
    ans = max(dp[N][j], ans)

print(ans)