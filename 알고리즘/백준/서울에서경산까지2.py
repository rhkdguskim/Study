# https://www.acmicpc.net/problem/14863
# 배낭문제와 유형이 똑같다.
# 걸리는 시간을 가방에 넣을 수 있는 최대 무게라고 생각하면 된다.
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 0번째 idx는 Dummy 값이다.

walk = []
bike = []
for _ in range(N):
    a, b, c , d = map(int, input().split())
    walk.append((a, b)) # 시간, 모금액
    bike.append((c, d)) # 시간, 모금액
    

dp = [[-1 for _ in range(K+1)] for _ in range(N)]
def dfs(idx, time):
    if time < 0:
        return -int(1e9)
    
    if idx == N:
        return 0
    
    if dp[idx][time] != -1:
        return dp[idx][time]
    
    dp[idx][time] = max(dfs(idx+1, time-bike[idx][0]) + bike[idx][1], dfs(idx+1, time-walk[idx][0]) + walk[idx][1])
    return dp[idx][time]


print(dfs(0, K))