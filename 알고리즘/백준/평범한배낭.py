# https://www.acmicpc.net/problem/12865
# 1개~N개의 물건을 넣어보면서 자기자신을 넣을경우 넣지 않을경우중 무게의 가치의 최대값을 찾는다.
# 예를들어 dp[1]이라면 1번째 아이템까지 넣은 가치의 최대값을, dp[2] 라면 1~2번째 아이템까지 넣은 가치의 최대값을 갱신해준다.
# 시간복잡도 : O(N*W)
import sys
input = sys.stdin.readline
N ,K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
value = [0]
weight = [0]
for _ in range(N):
    w, v = map(int, input().split())
    value.append(v)
    weight.append(w)
    
# 명령문 방식
for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j-weight[i]] + value[i], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(max(dp[N]))


newdp = [[-1 for _ in range(K+1)] for _ in range(N+1)]
# 재귀방식
def knapsack(i, w):
    if w < 0: # 무게를 넣을 수 없는경우
        return -1e9
    
    if i == 0:
        return 0
    
    if newdp[i][w] != -1: # 이미 계산한 결과 메모리제이션
        return newdp[i][w]
    
    newdp[i][w] = max(knapsack(i-1, w-weight[i]) + value[i], knapsack(i-1, w)) # 자신을 넣어보거나, 넣지 않아보거나
    return newdp[i][w]
    
print(knapsack(N, K))