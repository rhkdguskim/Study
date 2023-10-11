# https://www.acmicpc.net/problem/19236
from pprint import pprint
import heapq
from copy import deepcopy

N = 4 # 4x4
graph = [[[] for _ in range(N)] for _ in range(N)]
direction = [(0, 0), (-1, 0), (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 1), (0, 1), (-1, 1)] # 자기자신, ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다.

fishqueue = [] # 물고기를 순서대로 움직일 큐

for i in range(N):
    temp = list(map(int, input().split()))
    j = 0
    for j in range(0,len(temp), 2):
        graph[i][j//2] = [temp[j], temp[j+1]] # 물고기번호, 물고기방향
        fishqueue.append((temp[j], temp[j+1], i , j)) # 물고기 번호와 방향, 좌표를 갖는 큐를 만든다.

# 1. 상어가 공간에 들어가 물고기를 먹는다.


# 시계반대방향 45도로 도는경우
def rotate(type):
    if type == len(direction)-1: # 마지막인경우
        return 1
    else:
        return type + 1

def canmoveshark():
    global ans
    if graph[0][0][0] == 0: # 0은 빈칸으로 표현된다.
        return None

    ans += graph[0][0][0] # 먹어버린 가중치 추가
    graph[0][0][0] = 20 # 물고기를 먹어버린뒤, 상어의 위치를 표기한다.
    return graph[0][0][1] # 상어의 방향을 나타낸다.

# 상어가 이동가능한 물고기 리스트들을 만든다.
def fishlist(i, j, dir):
    dy,dx = direction[dir]
    queue = []
    for k in range(1, 4):
        ny, nx = dy * k + i, dx * k + j
        if N > ny >= 0 and N > nx >= 0 and graph[ny][nx] != 0: #물고기라면
            queue.append((ny, nx)) # 먹을 수 있는 후보를 탐색한다.

    return queue


def movefish():
    newqueue = []

    fishqueue.sort()
    while fishqueue:
        num, dir, i, j = fishqueue.pop()

        visited = [False for _ in range(9)]
        visited[0] = True

        while True: # 움직일수있는 경우까지 찾는다.
            print(dir)
            visited[dir] = True
            dy, dx = direction[dir]
            ny, nx = dy +i, dx + j
            #빈칸과 물고기가 있는칸은 이동 할 수 있다.
            if N > ny >=0 and N > nx >=0 and 20 > graph[ny][nx][0]: # 상어는 20으로 표현하겠음.
                # 탐색할 수 있는경우 물고기의 위치를 바꾼다.
                temp1, temp2 = graph[ny][nx][0], graph[ny][nx][1]# 물고기 번호, 방향

                # 물고기 자리를 바꾼다.
                graph[ny][nx][0] = num
                graph[ny][nx][1] = dir

                graph[i][j][0] = temp1
                graph[i][j][1] = temp2
                break
            elif all(visited):
                # 45도씩 회전하면서 다 돌았는데 갈 수 없는경우
                break
            else:
                dir = rotate(dir) # 방향을 회전시킨다.

    # 새로운 큐를 만든다.
    for i in range(N):
        for j in range(N):
            if graph[i][j][0] != 0 and graph[i][j] != 20:
                newqueue.append((graph[i][j][0], graph[i][j][1], i ,j))

    return newqueue # 새로운 물고기 큐 리턴한다.


ans = 0
def dfs(queue, visitedq):
    global visitedqueue
    if not queue:
        visitedqueue = deepcopy(visitedq)
        return visitedq

    # 물고기를 먹는다.
    result = 0
    i, j = queue.pop()
    fishnum = graph[i][j][0]
    newdir = graph[i][j][1]
    graph[i][j][0] = 0 # 물고기를 먹는다.
    newqueue = fishlist(i, j, newdir)
    visitedq.append((i,j))
    result = max(dfs(newqueue, visitedq), result)
    visitedq.pop()
    queue.append((i, j))
    graph[i][j][0] = fishnum

    return result

ans = 0
while True:
    c = canmoveshark()
    if c is None: # 상어가 더이상 움직일 수 없다면 끝난다.
        break

    fishqueue = movefish() # 물고기가 움직인다.
    maxeat = 0

    queue = fishlist(0, 0, c) # 상어가 먹을 수 있는 물고기 후보들
    visitedqueue = []

    dfs(queue, []) # 다 먹어버린다.
    for i, j in visitedqueue:
        ans += graph[i][j][1]
        graph[i][j][0] = 0

    graph[0][0][0] = 0 # 상어가 다시 집으로간다.

    fishqueue = movefish() # 물고기가 움직인다.