# https://www.acmicpc.net/problem/1018
# 흰색인경우와 검은색인경우 조건을 다 탐색하여 문제를 업데이트한다.
# (0,0)이 white인경우 (0,0)이 black 인경우
move = ((0,1), (1,0), (0, -1), (-1, 0))

N, M = map(int, input().split())
graph = []
CHAR = ["W", "B"]
WHITE = 0
BLACK = 1

def dfs(i, j, cur, visited):
    global cnt, h, w, h2, w2
    if graph[i][j] != cur:
        cnt += 1
    
    for dy, dx in move:
        ny, nx = i +dy, j+dx
        if h >= ny >= h2 and w >= nx >= w2 and not visited[ny][nx]:
            visited[ny][nx] = True
            if cur == CHAR[WHITE]:
                dfs(ny, nx, CHAR[BLACK], visited)
            else:
                dfs(ny, nx, CHAR[WHITE], visited)
            
    

minresult = N*M
for _ in range(N):
    graph.append(list(map(str, input())))
    
for i in range(N):
    for j in range(M):
        h, w, cnt = i+7, j+7, 0
        h2 , w2 = i, j
        #print(N,M ,h,w, cnt)
        if N > h >=0 and M > w >=0:
            visited = [[False for _ in range(M)] for _ in range(N)]
            #print(i,j, "시작")

            visited[i][j] = True
            dfs(i,j,'W', visited)
            #print(visited)
            #print("White",cnt)
            minresult = min(cnt, minresult)

            visited = [[False for _ in range(M)] for _ in range(N)]

            cnt = 0
            visited[i][j] = True
            dfs(i,j, 'B', visited)
            #print("Black",cnt)
            minresult = min(cnt, minresult)
        
print(minresult)