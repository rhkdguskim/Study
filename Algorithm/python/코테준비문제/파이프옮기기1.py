# https://www.acmicpc.net/problem/17070

# 다이나믹 프로그래밍 기법으로 벌집 승연이와 똑같은 문제이나 구현 문제가 더 복잡하다.
# 처음 출발은 가로 방향이다.
import sys
sys.setrecursionlimit(1000000)
type = ['H','V','C'] # 가로, 세로, 대각선
movetype = dict()
movetype['H'] = (((0,1, 'H'), (1,1, 'C'))) # 가로일때
movetype['V'] = ((1,0, 'V'), (1,1, 'C')) # 세로일때
movetype['C'] = ((0,1, 'H'), (1,0,'V'), (1,1,'C'))
dir = dict()
dir['H'] = 0
dir['V'] = 1
dir['C'] = 2
input = sys.stdin.readline

N = int(input())
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
def dfs(i,j, direction):
    if N > i >=0 and N > j >=0 :
        if i==N-1 and j == N-1: # 목표지점에 도달했을경우
            dp[dir[direction]][N-1][N-1]= 1
            return dp[dir[direction]][N-1][N-1]
        
        if dp[dir[direction]][i][j] != 0:
            return dp[dir[direction]][i][j]
        
        else: # 목표지점에 도달하지 않았을경우
            for dy, dx , move in movetype[direction]:
                ny = dy + i
                nx = dx + j
                
                if not (N > ny >=0 and N > nx >=0):
                    continue
                
                if move != 'C' and graph[ny][nx]:
                    continue
                
                if move == 'C':
                    if not (N > i+1 >=0 and N > j >=0):
                        continue
                    
                    if  not (N > i >=0 and N > j+1 >=0):
                        continue
                    
                    if graph[i+1][j] or graph[i][j+1] or graph[ny][nx]:
                        continue
                
                dp[dir[direction]][i][j] += dfs(ny, nx, move)
                
            return dp[dir[direction]][i][j]
    else:
        return 0

if graph[N-1][N-1]:
    print(0)
else:
    dp[dir["H"]][0][1] = dfs(0,1, "H")
    print(dp[dir["H"]][0][1] )