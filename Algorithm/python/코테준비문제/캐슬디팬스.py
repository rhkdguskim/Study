# https://www.acmicpc.net/problem/17135
# 1. 궁수가 적을 공격한다. 5 중에 3자리의 궁수를 뽑아서 최대 개수를 찾아야한다. 최대 개수를 찾았다면 그 최대개수를 테이블에 갱신시킨다.
# 2. 적이 이동한다. ( 적이 성을 침범한다면 게임이 종료, 또한 적이 다 죽었다면 게임이 종료 )
from copy import deepcopy
from itertools import combinations
from collections import deque
from pprint import pprint
import heapq

moves = [(-1, 0), (0, -1), (0, 1)]  # 세 방향으로만 갈 수 있다.

N, M, D = map(int, input().split()) # 행, 열, 공격범위
table = []
arrows = []

for i in range(M):
    arrows.append((N, i, N, i))

for _ in range(N):
    table.append(list(map(int, input().split())))
def attack(arrow, table):
    global answer
    queue = deque(arrow)
    killed = [[] for _ in range(M)]
    visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(M)]
    while queue:
        i, j, arrowy, arrowx = queue.popleft()
        for dy, dx in moves:
            ny = i + dy
            nx = j + dx
            if N > ny >= 0 and M > nx >= 0:
                distance = abs(ny - arrowy) + abs(nx - arrowx)
                if D >= distance and not visited[arrowx][ny][nx]:# 사냥할 수 있는 범위에 있다면 방문한다.
                    visited[arrowx][ny][nx] = True
                    if table[ny][nx] == 1:
                        heapq.heappush(killed[arrowx], (distance, ny, nx))

                    queue.append((ny, nx, arrowy, arrowx))

    # 모든 탐색이 끝나고 table에 갱신한다.
    #print(arrow)
    attacked = set()
    for arr in killed:
        temp = []
        while arr:
            dis, y, x = heapq.heappop(arr)
            #print(dis, y ,x)
            if temp:
                if dis > temp[0][2]:
                    break
                else:
                    temp.append((x, y, dis))
            else:
                temp.append((x, y, dis))
        if temp:
            temp.sort()
            attacked.add((temp[0][1], temp[0][0]))
            #print(temp[0][1], temp[0][0])
            table[temp[0][1]][temp[0][0]] = 0

    answer += len(attacked)

def isend(table):
    for i in range(N):
        for j in range(M):
            if table[i][j] == 1: # 적이 존재한다면 게임이 끝난게 아니다.
                return False

    # 적이 존재하지 않다면 게임이 종료된다.
    return True

def move(table):
    for i in range(N - 2, -1, -1): # 적을 한칸씩 밀려온다.
        table[i + 1] = table[i]

    table[0] = [0 for _ in range(M)]

maxanswer = 0
for arrow in combinations(arrows, 3):  # 궁수의 경우의 수를 계산한다.
    answer = 0
    newtable = deepcopy(table)
    while True: # O(N)
        if isend(newtable):
            break
        attack(arrow, newtable)
        #pprint(newtable)
        if isend(newtable): # O(N*M)
            break
        move(newtable) # O(N*M)
        #pprint(newtable)
        #print(answer)
        #print("----------")
    if answer > maxanswer:
        #pprint(arrow)
        #pprint(newtable)
        maxanswer = answer

print(maxanswer)