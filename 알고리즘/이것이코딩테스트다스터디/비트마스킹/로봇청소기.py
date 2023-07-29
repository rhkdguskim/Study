# https://www.acmicpc.net/problem/4991
# 모든 경우의수를 다 탐색해보아 최소값을 구한다.
# 최소값보다 커진다면 탐색을 중지한다.
# 탐색해야하는 더러운 위치가 (0,0), (1,0), (0,1), (1,1) 이 있다면 현재 나를 포함하는경우, 포함하지 않는경우를 비트마스킹 하여 경우의수를 탐색한다.
from sys import stdin
from collections import deque
input = stdin.readline
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = int(10e9)


def dfs(startidx, visited, cost):
    if cost > minvalue:
        return INF

    if visited == (1 << len(dirtylist)) - 1:  # 모든 곳을 방문했다면
        return cost
 
    min_cost = INF
    for endidx in range(len(dirtylist)):
        if not visited & (1 << endidx):
            new_visited = visited | (1 << endidx)
            new_cost = cost + bfs(startidx, endidx)
            min_cost = min(min_cost, dfs(endidx, new_visited, new_cost))

    return min_cost


def bfs(startidx, endidx):  # start 부터 end 까지 최소거리 탐색 , 만약 가지 못한다면 INF
    if dp[startidx][endidx] != None:
        return dp[startidx][endidx]
    
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque()
    y, x = dirtylist[startidx]
    end_y, end_x = dirtylist[endidx]
    queue.append([y, x, 0])
    while queue:
        i, j, cost = queue.popleft()
        for dy, dx in move:
            ny = dy + i
            nx = dx + j
            if h > ny >= 0 and w > nx >= 0 and not visited[ny][nx] and not graph[ny][nx] == 'x':
                visited[ny][nx] = True
                if ny == end_y and nx == end_x:
                    dp[startidx][endidx] = cost + 1
                    return dp[startidx][endidx]

                queue.append([ny, nx, cost + 1])

    dp[startidx][endidx] = INF
    return dp[startidx][endidx]


while True:
    w, h = map(int, input().split())  # 너비, 높이
    if w == 0 and h == 0:  # 0,0이 주어지면 종료한다.
        break
    else:
        graph = []
        dirtylist = []
        
        start = 0
        for i in range(h):
            char = list(map(str, input()))
            for j in range(len(char)):
                if char[j] == '*' or char[j] == 'o':
                    dirtylist.append([i, j])
                if char[j] == 'o':
                    start = len(dirtylist) - 1
            graph.append(char)
            
        minvalue = INF
       
        dp = [[None for _ in range(len(dirtylist))] for _ in range(len(dirtylist))]
        for endidx in range(len(dirtylist)):
            visited = 1 << start
            if not visited & (1 << endidx):
                visited |= 1 << endidx
                minvalue = min(minvalue, dfs(endidx, visited, bfs(start, endidx)))

        if minvalue != INF:
            print(minvalue)
        else:
            print(-1)
