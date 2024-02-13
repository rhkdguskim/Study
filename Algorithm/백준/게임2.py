# https://www.acmicpc.net/problem/1103
import sys
input = sys.stdin.readline
INF = int(1e5)
sys.setrecursionlimit(int(1e5))

N, M = map(int, input().split())
table = [str(input()) for _ in range(N)]

def is_range(y, x):
    return N > y >=0 and M >x >=0

dp = [[-1 for _ in range(M)] for _ in range(N)]

def dfs(y, x):
    if not is_range(y, x):
        return 0
    
    if table[y][x] == 'H':
        return 0
    
    if visited[y][x]:
        return INF
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    visited[y][x] = True
    cur_num = int(table[y][x])
    
    dp[y][x] = 0
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny, nx = dy*cur_num + y, dx*cur_num + x
        dp[y][x]  = max(dp[y][x], dfs(ny, nx) + 1)
    
    visited[y][x] = False
    
    return dp[y][x] 

visited = [[False for _ in range(M)] for _ in range(N)]
ans = dfs(0, 0)

if ans >= INF:
    print(-1)
else:
    print(ans)