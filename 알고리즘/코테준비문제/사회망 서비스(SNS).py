# https://www.acmicpc.net/problem/2533
# 내가 얼리어뎁터이면 친구들은 얼리어뎁터가 아니다.
# 내가 얼리어뎁터라면 친구들은 얼리어뎁터일수도있고 아닐수도 있다.
import sys
sys.setrecursionlimit(10 ** 9)
N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b  = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
dp = [[0 for _ in range(2)] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
def dfs(node):
    visited[node] = True
    if len(graph[node]) != 0:
        for newnode in graph[node]:
            if not visited[newnode]:
                dfs(newnode)
                dp[node][0] += dp[newnode][1] # 내가 얼리어뎁터가 아니라면 친구들이 얼리어뎁터이어야한다.
                dp[node][1] += min(dp[newnode][0], dp[newnode][1]) # 내가 얼리어뎁터라면 친구들은 얼리어뎁터일수도있고 아닐수도 있다. 
        
        dp[node][1] += 1 # 자기자신이 얼리어뎁터이다.
    else: # 자식이 없다면
        dp[node][0] = 0 # 얼라어답터가 아니다
        dp[node][1] = 1 # 얼리어답터 이다.
 
dfs(1)
print(min(dp[1][0], dp[1][1]))