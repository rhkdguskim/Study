# https://www.acmicpc.net/problem/1103
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

dp =[[0 for _ in range(M)] for _ in range(N)]
move = [(0,1), (0,-1), (1,0), (-1,0)]

flag = False
def dfs(i, j, visited):
    global flag
    
    if flag:
        return -1
    
    if i < 0 or i > N-1 or j <0 or j > M-1 or graph[i][j] == 'H':
        return 0
    
    if dp[i][j] != 0:
        return dp[i][j]
    
    for m in range(len(move)):
        ny, nx = move[m][0]*int(graph[i][j]) + i, move[m][1]*int(graph[i][j]) + j
        if (ny, nx) in visited: 
            flag = True
            return -1
        
        visited.append((ny, nx))
        dp[i][j] = max(dfs(ny, nx, visited)+1 , dp[i][j])
        visited.pop()
    
    return dp[i][j]

ans = dfs(0,0, [(0,0)])
if flag:
    print(-1)
else:
    print(ans)