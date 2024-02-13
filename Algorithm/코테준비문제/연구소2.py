# https://www.acmicpc.net/problem/17141
move = [(0,1), (0, -1), (1, 0), (-1, 0)]
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
EMPTY = 0
WALL = 1
CANVIRUS = 2
VIRUS = 3
totalspread = 0
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == EMPTY or temp[j] == CANVIRUS:
            totalspread += 1
    graph.append(temp)

ans = N*N
def dfs(idx, graph, virus):
    global ans
    if len(virus) == M:
        graph = deepcopy(graph)
        temp, cnt = spreadvirus(graph, virus)
        #print(virus)
        if cnt == totalspread - M:
            ans = min(temp, ans)
        return

    for n in range(idx, N*N):
        i = n // N
        j = n % N
        if graph[i][j] == CANVIRUS:
            graph[i][j] = VIRUS
            virus.append((i,j))
            dfs(i*N + j+1, graph, virus)
            virus.pop()
            graph[i][j] = CANVIRUS
def spreadvirus(graph, virus):
    visit = [[False for _ in range(N)] for _ in range(N)]
    maxcost = 0
    queue = deque()
    cnt = 0
    for i, j in virus:
        queue.append((i, j, 0))
        visit[i][j] = True

    while queue:
        y, x, cost = queue.popleft()
        for dy, dx in move:
            ny, nx = dy +y, dx + x
            if N > ny >= 0 and N > nx >=0 and not visit[ny][nx] and (graph[ny][nx] == EMPTY or graph[ny][nx] == CANVIRUS):
                visit[ny][nx] = True
                graph[ny][nx] = VIRUS
                queue.append((ny, nx, cost + 1))
                maxcost = max(cost + 1, maxcost)
                cnt += 1

    return maxcost, cnt

dfs(0, graph, [])
if ans == N*N:
    print(-1)
else:
    print(ans)