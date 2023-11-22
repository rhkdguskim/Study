#https://www.acmicpc.net/problem/11438
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))
LOG = 21 # 2^20 = 1,000,000
N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a , b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depth = [0 for _ in range(N+1)]
visited = [False for _ in range(N+1)]
dp = [[0 for _ in range(LOG)] for _ in range(N+1)]

def dfs(rootnode, cost):
    depth[rootnode] = cost
    visited[rootnode] = True
    for childnode in graph[rootnode]:
        if not visited[childnode]:
            dp[childnode][0] = rootnode # 제일 가까운 조상초기화
            dfs(childnode, cost+1)
            
                    
def lca(a,b):
    # b가 더 깊도록 설정
    if depth[a] > depth[b]: # 노드 a가 b보다 깊이가 깊으면 스위치
        a,b = b,a
    
    for i in range(LOG -1, -1, -1):
        if depth[b] - depth[a] & (1 << i): # depth가 7일때 3번 점프한다.
            b = dp[b][i]
        
    if a == b:
        return a    
            
    for i in range(LOG -1, -1 , -1):
        if dp[a][i] != dp[b][i]:
            a = dp[a][i]
            b = dp[b][i]
    
    return dp[a][0]

dfs(1,0)
for i in range(1, LOG):
    for j in range(1, N+1):
        dp[j][i] = dp[dp[j][i-1]][i-1]
    
M = int(input())

for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a,b))