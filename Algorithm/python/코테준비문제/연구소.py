# https://www.acmicpc.net/problem/14502
from collections import deque
from copy import deepcopy
import sys
from pprint import pprint
input = sys.stdin.readline
N, M = map(int, input().split())
moves = [(1,0), (-1,0), (0,1), (0,-1)]

EMPTY = 0
WALL = 1
VIRUS = 2

graph = []
for _ in range(N):
    graph.append(list(map(int ,input().split())))


def virus(graph):
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] == VIRUS and not visited[i][j]:
                visited[i][j] = True
                queue = deque()
                queue.append((i, j))
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in moves:
                        ny, nx = y + dy, x + dx
                        if N > ny >=0 and M > nx >=0 and not visited[ny][nx] and graph[ny][nx] == EMPTY: # 빈공간을 바이러스로 만든다.
                            visited[ny][nx] = True
                            graph[ny][nx] = VIRUS
                            queue.append((ny, nx))

def safearea(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
           if graph[i][j] == EMPTY:
                cnt += 1

    return cnt

ans = 0
def dfs(idx, graph, wall):
    global ans
    if wall == 3:
        graph = deepcopy(graph)
        virus(graph)
        cnt = safearea(graph)
        #pprint(graph)
        ans = max(ans, cnt)
        return

    i = idx // M
    j = idx % N
    for y in range(N):
        for x in range(M):
            if graph[y][x] == EMPTY:
                graph[y][x] = WALL
                dfs(idx+1, graph, wall + 1)
                graph[y][x] = EMPTY

dfs(0, graph, 0)
print(ans)
