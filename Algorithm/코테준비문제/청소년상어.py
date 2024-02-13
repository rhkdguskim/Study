# https://www.acmicpc.net/problem/19236
from pprint import pprint
# 1. 상어가 0,0으로 이동한다. 물고기를 먹어버린다. 물고기 방향으로 바뀐다.
# 2. 물고기가 작은 순서부터 이동한다.
# 3.
from copy import deepcopy
EMPTY = -1
SHARK = 20
N = 4 # 4x4
graph = [[[] for _ in range(N)] for _ in range(N)]
direction = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)] # ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다.

for i in range(N):
    temp = list(map(int, input().split()))
    j = 0
    for j in range(0,len(temp), 2):
        graph[i][j//2] = [temp[j], temp[j+1]-1] # 물고기번호, 물고기방향

# 상어가 먹을 수 있는 물고기 리스트
def fishlist(i, j, dir, graph):
    dy, dx = direction[dir]
    queue = []
    for k in range(1, N):
        ny = (dy * k) + i
        nx = (dx * k) + j
        if N > ny >= 0 and N > nx >= 0 and graph[ny][nx][0] != EMPTY: #물고기라면
            queue.append((ny, nx)) # 먹을 수 있는 후보를 탐색한다.

    return queue

def findfish(fishnum, graph):
    for i in range(N):
        for j in range(N):
            if graph[i][j][0] == fishnum:
                return (i, j)
def movefish(i, j, graph):
    visited = [False for _ in range(len(direction))]
    dir = graph[i][j][1]

    while True: # 움직일수있는 경우까지 찾는다.
        visited[dir] = True
        dy, dx = direction[dir]
        ny, nx = dy + i, dx + j
        #빈칸과 물고기가 있는칸은 이동 할 수 있다.
        if N > ny >=0 and N > nx >=0 and SHARK != graph[ny][nx][0]: # 상어가 아닌칸과, 범위를 벗어나는 경우
            temp1, temp2 = graph[ny][nx][0], graph[ny][nx][1] # 물고기 번호, 방향
            # 물고기 자리를 바꾼다.
            graph[ny][nx][0] = graph[i][j][0]
            graph[ny][nx][1] = dir

            graph[i][j][0] = temp1
            graph[i][j][1] = temp2
            break

        if all(visited):
            # 45도씩 회전하면서 다 돌았는데 갈 수 없는경우
            break

        dir = (dir + 1) % len(direction)


def dfs(i, j, graph, total):
    global ans
    graph = deepcopy(graph)
    # 상어가 물고기를 먹는다.
    graph[i][j][0] = SHARK
    shark_direction = graph[i][j][1]

    # 물고기가 움직인다.
    for n in range(1, 17): # 1번 물고기부터 16번 물고기 까지 차례대로 움직인다.
        fish = findfish(n, graph)
        if fish:
            ny_fish, nx_fish = fish[0], fish[1]
            movefish(ny_fish, nx_fish, graph)

    # 상어가 먹을수 있는 물고기 리스트들을 구한다.
    graph[i][j][0] = EMPTY
    fish_list = fishlist(i, j, shark_direction, graph)
    #pprint(fish_list)
    #pprint(graph)
    if fish_list:
        for ny_shark, nx_shark in fish_list: # 상어가 먹을 수 있는 모든 경우의 수를 탐색한다.
            dfs(ny_shark, nx_shark, graph, total + graph[ny_shark][nx_shark][0])
    else: # 먹을 수 있는 경우의 수가 없다면 최대값을 갱신해준다.
        ans = max(ans, total)
        return

ans = 0
dfs(0, 0, graph, graph[0][0][0])

print(ans)
