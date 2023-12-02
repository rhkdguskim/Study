# https://www.acmicpc.net/problem/3109
# 맨 첫번째 행부터 출발할경우 이동시에 우선순위
# 1) 오른쪽 위
# 2) 오른쪽
# 3) 오른쪽 아래

# 위의 그리디 방식으로 DFS, BFS탐색을 했을때, 매일 처음에 목적지에 도착한 도착지를 방문처리 하면 된다.

import sys
input = sys.stdin.readline

moves = [(-1, 1), (0, 1), (1, 1)] # 위, 중간 ,아래

R, C  = map(int, input().split()) # 행, 열
graph = [list(input().strip()) for _ in range(R)]

def dfs(i, j, graph):
    if j == C-1: # 도착지에 도달하면
        return True
    
    for dy, dx in moves:
        ny, nx = i + dy, j + dx
        if R > ny >= 0 and C > nx >= 0 and graph[ny][nx] != 'x':
            graph[ny][nx] = 'x' # 무조건 x처리 해준다. 왜냐하면, 갈 수 없는 경로를 또 체크하는 경우가 생기기때문이다.
            if dfs(ny, nx, graph): # 경로를 찾은경우 바로 return 한다.
                return True
    
    # 경로를 탐색 했는데 결과를 찾을 수 없을경우
    return False

ans = 0
for i in range(R):
    if dfs(i, 0, graph):
        ans += 1
        
print(ans)