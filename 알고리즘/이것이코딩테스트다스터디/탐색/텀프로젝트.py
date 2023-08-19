# https://www.acmicpc.net/problem/9466
import sys
sys.setrecursionlimit(100001)
T = int(input())


def dfs(student, root):
    if student == graph[student]: # 자기자신을 뽑는경우
        dp[student] = 0
        return dp[student]
    
    if graph[student] == root: # 사이클이 한번 돌은경우 (이들은 서로 그룹이 된다.)
        dp[student] = 1
        return dp[student]
    
    dp[student] = dfs(graph[student], root)
    return dp[student]

for _ in range(T):
    n = int(input())
    graph = [0] + list(map(int, input().split())) # 0을 추가하는이유는 0번인 학생이 없기 때문
    dp = [None for _ in range(n+1)]
    for i in range(1, n+1):
        if dp[i] is None:
            dp[i] = dfs(i, i)
    print(dp.count(1))