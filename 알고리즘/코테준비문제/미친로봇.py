# https://www.acmicpc.net/problem/1405
percent = list(map(int, input().split())) # 동 서 남 북 각 확률 만큼 방문한다.
N = percent.pop(0)
SIZE = 2*N+1
graph = [[0 for _ in range(SIZE)] for _ in range(SIZE)] # 동서남북을 움직이기 위한 2N+1 배열 생성
move = ((0, 1), (0, -1), (1, 0), (-1, 0)) # 동, 서, 남, 북

ans = 0
def dfs(i,j,p, depth):
    global ans
    if depth == N:
        ans += p
        return

    for m in range(len(move)):
        ny, nx = i + move[m][0], j + move[m][1]
        if SIZE > ny >= 0 and SIZE > nx >= 0 and graph[ny][nx] == 0:
            graph[ny][nx] = 1
            newp = percent[m] / 100
            dfs(ny, nx, p*newp, depth+1)
            graph[ny][nx] = 0


for i in range(4):
    graph[N][N] = 1
    dfs(N, N, percent[i] / 100, 0)
    graph[N][N] = 0

print(ans)






