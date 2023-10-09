# https://www.acmicpc.net/problem/15685
MAX_SIZE = int(101)
from copy import deepcopy
from pprint import pprint
move = [(0,1), (-1,0), (0,-1), (1,0)]
move2 = [(0,1), (1,0), (1,1)]
N = int(input())
table = [[0 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]

def getsqure():
    cnt = 0
    for i in range(MAX_SIZE):
        for j in range(MAX_SIZE):
            if table[i][j]:
                squere = [False for _ in range(3)]
                for k in range(len(move2)):
                    ny = move2[k][0] + i
                    nx = move2[k][1] + j
                    if MAX_SIZE > ny >=0 and MAX_SIZE > nx >= 0 and table[ny][nx]:
                        squere[k] = True

                if all(squere):
                    cnt += 1

    return cnt


def rotate(idx):
    if idx == 3:
        return move[0]
    else:
        return move[idx+1]
def dragon(i,j, queue, depth):
    if depth == g: # 드래곤 세대 까지만 탐색
        return queue

    newqueue = []
    temp = reversed(queue)
    for m in temp: # 기존에 그렸던 것을 회전하여 생성한다.
        newqueue.append(rotate(move.index(m)))

    # 좌표를 움직인다.
    for ny, nx in newqueue:
        i = ny + i
        j = nx + j

    return dragon(i,j, deepcopy(queue+newqueue), depth+1)

visitqueue = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    ny = y + move[d][0]
    nx = x + move[d][1]
    queue = dragon(ny, nx, [move[d]], 0)

    starty = y
    startx = x
    table[y][x] = 1
    for ny, nx in queue:
        starty = ny + starty
        startx = nx + startx
        table[starty][startx] = 1

print(getsqure())



