# https://www.acmicpc.net/problem/14863
# 배낭문제와 유형이 똑같다.
# 걸리는 시간을 가방에 넣을 수 있는 최대 무게라고 생각하면 된다.
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 0번째 idx는 Dummy 값이다.

walk = [(0,0)]
bycle = [(0,0)]
for _ in range(N):
    a, b, c , d = map(int, input().split())
    walk.append((a, b)) # 시간, 모금액
    bycle.append((c, d)) # 시간, 모금액
    
dp = [[[0 for _ in range(2)] for _ in range(K+1)] for _ in range(N+1)]

ans = 0
for i in range(1, N+1):
    for j in range(1, K+1):
       # 걸어서 간다.
        # 직전에 자전거를 타고온경우와 걸어온경우중 더 큰값을 갱신
        if K >= j+walk[i][0]:
            dp[i][j+walk[i][0]][0] = max(dp[i-1][j+walk[i][0]][0], dp[i-1][j+walk[i][0]][1]) + walk[i][1]
        else:
            if walk[i][0] > j:
                dp[i][j-walk[i][0]][0] = max(dp[i-1][walk[i][0]-j][0], dp[i-1][walk[i][0]][1]-j) + walk[i][1]
            
    # 자전거 타고 간다.
        # 직전에 자전거를 타고온경우와 걸어온경우중 더 큰값을 갱신
        if K >= j+bycle[i][0]:
            dp[i][j+bycle[i][0]][1] = max(dp[i-1][j+bycle[i][0]][0], dp[i-1][j+bycle[i][0]][1]) + bycle[i][1]
        else:
            if bycle[i][0] > j:
                dp[i][bycle[i][0]-j][1] = max(dp[i-1][bycle[i][0]-j][0], dp[i-1][bycle[i][0]][1]-j) + bycle[i][1]

        ans = max(ans, dp[i][j][0], dp[i][j][1])
#print(dp)
print(ans)d