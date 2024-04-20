# https://www.acmicpc.net/problem/2056
import sys
input = sys.stdin.readline

N = int(input())
in_degree = [0 for _ in range(N)]
edge = [[] for _ in range(N)]
time = [0 for _ in range(N)]
dp = [-1 for _ in range(N)]

def dfs(node):
    for child in edge[node]:
        in_degree[child] -= 1
        dp[child] = max(dp[child], dp[node]+time[child])
        if in_degree[child] <= 0:
            dfs(child)
            
def get_root():
    roots = []
    for n in range(N):
        if in_degree[n] == 0:
            roots.append(n)
            
    return roots

for i in range(N):
    temp = list(map(int, input().split()))
    time[i] = temp[0]
    in_degree[i] = temp[1]
    if temp[1]:
        for n in temp[2:]:
            edge[n-1].append(i)


roots = get_root()
for root in roots:
    dp[root] = time[root]
    dfs(root)

print(max(dp))