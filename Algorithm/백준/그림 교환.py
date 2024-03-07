# https://www.acmicpc.net/problem/1029
# i번째사람을 선택한경우 선택하지 않은경우로 나눈다.
# i번째사람에 j번째 사람에게 그림을 팔았을때의 최대 수 dp[i][j]
import sys
input = sys.stdin.readline


# 1 -> 2 -> 4-> 5
# 예를들어 현재까지의 값은  dp[5] =  key : (1,2,4) value : 4
# 1 -> 3 -> 6 -> 8 -> 9 dp[9] = key : (1,3,6,8) value : 5

N = int(input())
edge = [[] for _ in range(N+1)]
dp = [dict() for _ in range(N+1)]

for i in range(N):
    temp = list(str(input().strip()))
    for j in range(len(temp)):
        if i != j:
            edge[i+1].append((j+1, int(temp[j])))
            
def dfs(i, visited, cost, cnt):
    if visited in dp[i].keys():
        return dp[i][visited]
    
    dp[i][visited] = (cost, cnt)
    
    for new, new_cost in edge[i]:
        if new_cost >= dp[i][visited][0] and not (visited & (1 << new)):
            next_visited = visited | (1 << new)
            dp[new][next_visited] = dfs(new, next_visited, new_cost, cnt + 1)
            if dp[new][next_visited][1] > dp[i][visited][1]:
                dp[i][visited] = (dp[new][next_visited][0], dp[new][next_visited][1])
    
    return dp[i][visited]

print(dfs(1, (1 << 1), 0, 1)[1])
    