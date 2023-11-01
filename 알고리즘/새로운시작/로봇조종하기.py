# https://www.acmicpc.net/problem/2169
import sys
sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline
move = [(0,1), (0,-1), (1,0)]
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# dp 배열을 초기화합니다.
dp = [[-float('inf')] * M for _ in range(N)]
dp[0][0] = graph[0][0]

def dfs(i, j, visited, cost):
    dp[i][j] = cost
    
    for dy, dx in move:
        ny, nx = dy + i, dx + j
        if N > ny >=0 and M > nx >=0 and (ny, nx) not in visited:
            cost = dp[i][j] + graph[ny][nx]
            if cost > dp[ny][nx]:
                visited.append((ny, nx))
                dfs(ny, nx, visited, cost)
                visited.pop()
                
                
dfs(0,0,[(0, 0)],graph[0][0])
print(dp[N-1][M-1])