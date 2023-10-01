# https://www.acmicpc.net/problem/13460
from copy import deepcopy
from collections import deque
from pprint import pprint
types = ['L', 'R', 'U', 'D']
moves = [(0,-1), (0,1), (-1,0), (1,0)]
def search(type, table, queue):
    redfinished = False
    bluefinished = False
    newred = [0,0]
    newblue = [0,0]
    while queue:
        i, j, color = queue.popleft()
        dy, dx = moves[types.index(type)]
        ny, nx = i + dy, j + dx
        if N > ny >=0 and M > nx >=0:
            if table[ny][nx] == '.': # 방문 할 수 있다면
                table[ny][nx] = color # 이동한다.
                table[i][j] = '.' # 이동하면 빈칸으로 바꾸어 준다.
                queue.append((ny, nx, color))
            else: # 방문 할수 없다면.
                if table[ny][nx] == 'O':
                    table[i][j] = '.'  # 이동하면 빈칸으로 바꾸어 준다.
                    if color == 'R':
                        redfinished = True
                    else:
                        bluefinished = True

                if color == 'R':
                    newred[0] = i
                    newred[1] = j
                else:
                    newblue[0] = i
                    newblue[1] = j

    return redfinished, bluefinished, newred, newblue, table

def move(type, table, red, blue):
    newtable = deepcopy(table)
    queue = deque()
    if type == 'L':
        if red[1] > blue[1]: #블루가 더 작을경우 블루부터 탐색한다.
            queue.append((blue[0], blue[1], 'B'))
            queue.append((red[0], red[1], 'R'))
        else:
            queue.append((red[0], red[1], 'R'))
            queue.append((blue[0], blue[1], 'B'))
    elif type == 'R':
        if red[1] > blue[1]: # 블루가 더 작을경우 레드부터 탐색한다.
            queue.append((red[0], red[1], 'R'))
            queue.append((blue[0], blue[1], 'B'))
        else:
            queue.append((blue[0], blue[1], 'B'))
            queue.append((red[0], red[1], 'R'))
    elif type == 'U':
        if red[0] > blue[0]: # 블루부터 움직인다.
            queue.append((blue[0], blue[1], 'B'))
            queue.append((red[0], red[1], 'R'))
        else:
            queue.append((red[0], red[1], 'R'))
            queue.append((blue[0], blue[1], 'B'))
    elif type == 'D':
        if red[0] > blue[0]: # 레드부터 움직인다.
            queue.append((red[0], red[1], 'R'))
            queue.append((blue[0], blue[1], 'B'))
        else:
            queue.append((blue[0], blue[1], 'B'))
            queue.append((red[0], red[1], 'R'))

    return search(type, newtable, queue)

def dfs(depth, table, red, blue, oldmove):
    if depth > 10:
        return 11

    minvalue = 11
    for t in types:
        if oldmove == 'R' or oldmove == 'L':
            if t == 'R' or t == 'L':
                continue
        elif oldmove == 'U' or oldmove == 'D':
            if t == 'U' or t == 'D':
                continue

        redfinished, bluefinished, newred, newblue, newtable = move(t, table, red, blue)

        if redfinished or bluefinished:
            if redfinished and not bluefinished:
                return depth + 1
            else:
                return 11
        minvalue = min(dfs(depth + 1, newtable, newred, newblue, t), minvalue)

    return minvalue


N, M = map(int, input().split())

table = []
red = [0, 0]
blue = [0, 0]
for i in range(N):
    newlist = list(input())
    for j in range(M):
        if newlist[j] == 'R':
            red[0] = i
            red[1] = j
        elif newlist[j] == 'B':
            blue[0] = i
            blue[1] = j

    table.append(newlist)
answer = dfs(0, table, red, blue, '')

if answer == 11:
    print(-1)
else:
    print(answer)