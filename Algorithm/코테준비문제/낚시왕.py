# https://www.acmicpc.net/problem/17143
# 가로로 움직일때 (C-1)로 나누었을때 홀수이면 방향은 그대로, 짝수이면 방향은 반대로 바뀐다.
# 좌표는 홀수일때 (C-1) - (거리 % (C-1) )
# 짝수일때 (거리 % (C-1))

import sys
input = sys.stdin.readline

direction = [(),(-1,0), (1,0), (0,1), (0,-1)] # 위,아래,오른,왼

R, C, M = map(int, input().split()) # 행, 열, 상어수
table = [[[] for _ in range(C+1)] for _ in range(R+1)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    table[r][c] = [s,d,z] # 속력, 이동방향, 크기

start = 0
def move(start):
    return start+1

def catch_shark(table, cur, score):
    for i in range(1, R+1):
        if table[i][cur]: # 상어가 있다면
            #print(i,cur, table[i][cur][2])
            ans = score + table[i][cur][2] # 크기를 누적한다.
            table[i][cur] = []
            return ans

    return score # 상어가 없는경우

def move_shark(table):
    temp = [[[] for _ in range(C+1)] for _ in range(R+1)] # 중복상어 확인 배열
    for i in range(1, R+1):
        for j in range(1, C+1):
            if table[i][j]: # 상어가 있다면 상어를 움직인다.
                print("start",i,j, table[i][j][0])
                y,x, type = dfs(i, j, table[i][j][0], table[i][j][1]) # 값을 구하는 방법을 최적화 해야한다.
                table[i][j][1] = type
                print("end", y,x, type)
                if temp[y][x]: # 이미 상어가 존재한다면
                    if table[i][j][2] > temp[y][x][2]:
                        temp[y][x] = [table[i][j][0], table[i][j][1], table[i][j][2]]
                else:
                    temp[y][x] = [table[i][j][0], table[i][j][1], table[i][j][2]]

    return temp


def dfs(i,j, depth, type):
    if type == 1: # 위로 움직일때
        cost = depth + R - i
        if ((R-1) // cost) % 2 == 0: # 나누기 했을때 짝 수 일때 방향이 변경된다.
            type = 2
            return (R-1) % cost, j, type
        else: # 홀수일때는 방향이 변경되지 않는다.
            return (R-1)-((R - 1) % cost), j, type
    elif type == 2: # 아래로 움직일때
        cost = depth - (i + 1)
        if ((R-1) // cost) % 2 == 0:
            type = 1
            return (R-1) % cost, j, type
        else:
            return (R - 1) - ((R - 1) % cost), j, type
    elif type == 3: # 오른쪽으로 움직일때
        cost = depth - (j+1)
        if ((C-1) // cost) % 2 == 0:
            type = 4
            return (C-1) % cost, j, type
        else:
            return (C-1) - ((C-1)%cost), j, type
    elif type == 4: # 왼쪽으로 움직일때
        cost = depth + C - i
        if ((C-1) // cost) % 2 == 0:
            type = 3
            return (C-1) % cost, j, type
        else:
            return (C-1) - ((C-1)%cost), j, type






score = 0
cur = 0
#pprint(table)
while True:
    cur = move(cur)
    if cur > C:
        break

    score = catch_shark(table, cur, score)
    table = move_shark(table)
    #pprint(table)

print(score)