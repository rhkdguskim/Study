# https://www.acmicpc.net/problem/2157
# 1. 특정 위치에서 가는 점수를 초기화한다 ( 경유해서 가는 경우 제와 )
# 2. 이제 특정위치에서 다른위치로 가는경우를 계산한다 ( 경유해서 가는경우를 포함시켜야한다. )
# 예외조건
# 1. 항상 목적지가 커야한다 ( 1->2 로 가야한다. 그렇지 않다면 거리값을 0으로 초기화 )
# 2. M개 이하의 도시만 가능하게 예외처리 해야한다.
import sys
input = sys.stdin.readline

N, M ,K = map(int, input().split()) # 도시의 개수, M개 이하의 도시만 가능, 개설된 항공수,

eat_value = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(K):
    a, b, c = map(int, input().split())
    eat_value[a][b] = max(eat_value[a][b], c) # a에서 b로 갈 수 있는 가중치의 값
    
dp = [[[0,0] for _ in range(N+1)] for _ in range(N+1)] # a의 도시에서 b의 도시로 갈때 기내식의점수, 경유횟수

# 경유해서 가는 경우를 제외하고 dp 테이블을 초기화한다.
for i in range(1,N+1):
    for j in range(1, N+1):
        if i < j:
            if eat_value[i][j] != 0: # 만약 갈수있는 가중치의 값이 있다면
                dp[i][j][0] = max(dp[i][j][0], eat_value[i][j]) # 가중치를 추가한다.
                dp[i][j][1] = 1 # 경유 횟수를 증가시킨다.
                
# 경유를 해서 가는 경우를 계산하여 문제를 해결한다.
for i in range(1, N+1):
    for j in range(1, N+1):
        temp = dp[i][j][0]
        for m in range(i+1, j):
            if i < j and i < m and j > m:
                if M > dp[i][m][1] > 0 and M > dp[m][j][1] > 0 and M > dp[i][j][1] > 0: # 경유해서 가는경우가 있고, 경유 횟수를 넘지 않았더라면 초기화한다.
                    # 기존 바로가는 경우와 경유해서 가는경우중 최대값 갱신
                    cost = dp[i][m][0] + dp[m][j][0]
                    if cost > dp[i][j][0]:
                        dp[i][j][0] = cost
                        
        if dp[i][j][0] != temp: # 만약 경유해서 가는 경우의 수가 있다면 경유 횟수를 추가한다.
            dp[i][j][1] += 1
            
print(dp)
print(dp[1][N][0])