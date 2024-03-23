# https://www.acmicpc.net/problem/14442
import sys
from collections import deque
INF = sys.maxsize

input = sys.stdin.readline
N, M, K = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, list(str(input().strip())))))
    
def bfs():
    queue = deque()
    visited = [[[INF]*(K+1) for _ in range(M)] for _ in range(N)]
    queue.append((0, 0, K, 0))
    for i in range(K+1):
        visited[0][0][i] = 0
    
    while queue:
        y, x, wall, cost = queue.popleft()
        #print(y, x, wall, cost)
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = dy + y, dx + x
            if N > ny >=0 and M > nx >=0:
                new_cost = cost + 1
                # 그냥 이동하는경우
                if graph[ny][nx] == 0:
                    if visited[ny][nx][wall] > new_cost:
                        visited[ny][nx][wall] = new_cost
                        queue.append((ny, nx, wall, new_cost))
                # 벽을 부수고 이동하는경우
                else:
                    if visited[ny][nx][wall-1] > new_cost and wall > 0:
                        visited[ny][nx][wall-1] = new_cost
                        queue.append((ny, nx, wall-1, new_cost))

    return min(visited[N-1][M-1])

ans = bfs()
if ans == INF:
    print(-1)
else:
    print(ans+1)