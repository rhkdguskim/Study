# https://www.acmicpc.net/problem/2637
# 기본부품은 부품간의 관계가 없는경우이다.
# 값을 계산했다는 flag(1차원)와 dp 테이블(2차원)을 둔다.
# 기본부품은 자기자신에게 가중치를 1을 둔다.

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

toy = [[] for _ in range(N+1)]
for _ in range(M):
    X, Y, K = map(int, input().split())
    toy[X].append((Y, K)) # 기본부품 Y가 K개 필요하다.
    

calculated = [False for _ in range(N+1)]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
def dfs(item):
    #print("item", item)
    if not toy[item]: # 기본부품인경우
        dp[item][item] = 1
        calculated[item] = True
        return dp[item]
    
    if calculated[item]:
        return dp[item]
    
    for new_item in toy[item]:
        temp = dfs(new_item[0])
        for i in range(N):
            dp[item][i] += temp[i] * new_item[1]
    
    calculated[item] = True
    return dp[item]

ans = dfs(N)
for i, r in enumerate(ans):
    if r:
        print(i, r)