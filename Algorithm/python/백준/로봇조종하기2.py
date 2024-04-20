import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e9))

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
INF = -int(1e9)

dp = [[[INF for _ in range(3)] for _ in range(M)] for _ in range(N)]
moves = [(0,-1), (0,1), (1,0)]
LEFT = 0
RIGHT = 1
DOWN = 2

def dfs(i, j, z):
    if dp[i][j][z] != INF:
        return dp[i][j][z]

    if i == N-1 and j == M-1:
        dp[i][j][z] = graph[i][j]
        return dp[i][j][z]
    
    dp[i][j][z] = graph[i][j]

    max_value = INF
    # 상, 하, 우로 이동
    for m in range(len(moves)):
        if (m == LEFT and z == RIGHT) or (m == RIGHT and z == LEFT):
            continue
        
        ny, nx = moves[m][0] + i, moves[m][1] + j
        
        if N > ny >= 0 and M > nx >= 0:
            max_value = max(dfs(ny,nx,m), max_value)
    
    dp[i][j][z] += max_value
    return dp[i][j][z]
        

print(dfs(0, 0, RIGHT))