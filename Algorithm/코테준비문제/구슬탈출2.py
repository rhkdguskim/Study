# https://www.acmicpc.net/problem/13460
from copy import deepcopy
from collections import deque
from pprint import pprint

types = ['L', 'R', 'U', 'D']
moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def search(type, table, queue):
    newred = [0, 0]
    newblue = [0, 0]
    while queue:
        i, j, color = queue.popleft()
        dy, dx = moves[types.index(type)]
        ny, nx = i + dy, j + dx
        if N > ny >= 0 and M > nx >= 0:
            if table[ny][nx] == '.':  # 방문 할 수 있다면
                table[ny][nx] = color  # 이동한다.
                table[i][j] = '.'  # 이동하면 빈칸으로 바꾸어 준다.
                queue.append((ny, nx, color))
            else:  # 방문 할수 없다면.
                if table[ny][nx] == 'O': # 구슬이 안으로 들어갔다면
                    table[i][j] = '.'  # 이동하면 빈칸으로 바꾸어 준다.
                    if color == 'R':
                        newred[0] = ny
                        newred[1] = nx
                    else:
                        newblue[0] = ny
                        newblue[1] = nx
                else:
                    if color == 'R':
                        newred[0] = i
                        newred[1] = j
                    else:
                        newblue[0] = i
                        newblue[1] = j

    return newred, newblue, table


def move(type, table, red, blue):
    newtable = deepcopy(table)
    queue = deque()
    if type == 'L':
        if red[1] > blue[1]:  # 블루가 더 작을경우 블루부터 탐색한다.
            queue.append((blue[0], blue[1], 'B'))
            queue.append((red[0], red[1], 'R'))
        else:
            queue.append((red[0], red[1], 'R'))
            queue.append((blue[0], blue[1], 'B'))
    elif type == 'R':
        if red[1] > blue[1]:  # 블루가 더 작을경우 레드부터 탐색한다.
            queue.append((red[0], red[1], 'R'))
            queue.append((blue[0], blue[1], 'B'))
        else:
            queue.append((blue[0], blue[1], 'B'))
            queue.append((red[0], red[1], 'R'))
    elif type == 'U':
        if red[0] > blue[0]:  # 블루 부터 움직인다.
            queue.append((blue[0], blue[1], 'B'))
            queue.append((red[0], red[1], 'R'))
        else:
            queue.append((red[0], red[1], 'R'))
            queue.append((blue[0], blue[1], 'B'))
    elif type == 'D':
        if red[0] > blue[0]:  # 레드부터 움직인다.
            queue.append((red[0], red[1], 'R'))
            queue.append((blue[0], blue[1], 'B'))
        else:
            queue.append((blue[0], blue[1], 'B'))
            queue.append((red[0], red[1], 'R'))

    return search(type, newtable, queue)


def dfs(depth, table, red, blue, oldmove):
    global goal
    if depth > 10:
        return 11

    if (goal[0] == red[0] and goal[1] == red[1]) or (goal[0] == blue[0] and goal[1] == blue[1]): # 빨간색공이 도달했다면
        if goal[0] == blue[0] and goal[1] == blue[1]: # 파란색공도 도달했다면 실패
            return 11
        elif goal[0] == red[0] and goal[1] == red[1]: # 빨간색공이 도달했다면
            return depth
        else:
            return 11

    minvalue = 11
    for t in types:
        if oldmove == 'R' or oldmove == 'L':
            if t == 'R' or t == 'L':
                continue
        elif oldmove == 'U' or oldmove == 'D':
            if t == 'U' or t == 'D':
                continue

        newred, newblue, newtable = move(t, table, red, blue)
        #print(newred, newblue)
        minvalue = min(dfs(depth + 1, deepcopy(newtable), newred, newblue, t), minvalue)

    return minvalue


N, M = map(int, input().split())

table = []
red = [0, 0]
blue = [0, 0]
goal = [0, 0]
for i in range(N):
    newlist = list(input())
    for j in range(M):
        if newlist[j] == 'R':
            red[0] = i
            red[1] = j
        elif newlist[j] == 'B':
            blue[0] = i
            blue[1] = j
        elif newlist[j] == 'O':
            goal[0] = i
            goal[1] = j

    table.append(newlist)
answer = dfs(0, deepcopy(table), red, blue, '')

if answer == 11:
    print(-1)
else:
    print(answer)
