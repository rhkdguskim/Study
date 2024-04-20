# https://www.acmicpc.net/problem/4485
move = ((0,1), (1,0), (0,-1), (-1,0))
import heapq
cnt = 1
while True:
    N = int(input())
    if N == 0:
        break

    INF = N*N*9 + 1
    graph = [list(map(int, input().split())) for _ in range(N)]
    queue = []
    visit = [[INF for _ in range(N)] for _ in range(N)]
    visit[0][0] = 0
    heapq.heappush(queue, (graph[0][0], 0 ,0))
    while queue:
        cost, i, j = heapq.heappop(queue)

        if i == N-1 and j == N-1:
            break

        for dy, dx in move:
            ny, nx = dy + i, dx + j
            if N > ny >= 0 and N > nx >= 0 and visit[ny][nx] > cost + graph[ny][nx]: # 거리가 최단거리가 아닐경우 방문한다.
                newcost = cost + graph[ny][nx]
                visit[ny][nx] = newcost
                heapq.heappush(queue, (newcost, ny, nx))

    print("Problem {}: {}".format(cnt, visit[N-1][N-1]))
    cnt += 1
