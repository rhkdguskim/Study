# https://www.acmicpc.net/problem/2169
import sys
INF = -int(1e9)

input = sys.stdin.readline
move = [(0,1), (0,-1), (1,0)]
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


dp = [[INF for _ in range(M)] for _ in range(N)]
dp[0][0] = graph[0][0]
# 처음에는 오른쪽으로 가는 방향이 제일 최대값이다.
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + graph[0][i]
    
# 왼쪽에서 온경우, 오른쪽에서 온경우를 모두 비교해보아 최대값을 갱신한다.
for i in range(1, N):
    left = [dp[i-1][j] + graph[i][j] for j in range(M)]
    right = [dp[i-1][j] + graph[i][j] for j in range(M)]
    
    # 위에서 내려온경우, 오른쪽에서 온경우 중 최대값
    for j in range(1, M):
        right[j] = max(right[j], right[j-1] + graph[i][j])
        
    # 위에서 내려온경우, 왼쪽에서 온경우 중 최대값
    for j in range(M-2, -1, -1):
        left[j] = max(left[j], left[j+1] + graph[i][j])
        
    for j in range(M):
        dp[i][j] = max(left[j], right[j])

print(dp[N-1][M-1])