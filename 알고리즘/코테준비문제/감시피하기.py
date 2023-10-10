# https://www.acmicpc.net/problem/18428
from pprint import pprint

N = int(input())
table = [[None for _ in range(N)] for _ in range(N)]
move = ((0, 1), (1, 0), (0, -1), (-1, 0))
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

TEACHER = 'T'
STUDENT = 'S'
EMPTY = 'X'
OBSTACLE = 'O'

teacher = []

for i in range(N):
    temp = list(map(str, input().split()))
    for j in range(len(temp)):
        if temp[j] == TEACHER:
            teacher.append((i, j))

        table[i][j] = temp[j]
def dfs(i, j, type):
    dy = i + move[type][0]
    dx = j + move[type][1]

    if type == UP and 0 > dy:
        return True

    elif type == DOWN and dy >= N:
        return True

    elif type == RIGHT and dx >= N:
        return True

    elif type == LEFT and 0 > dx:
        return True
    else:
        if table[dy][dx] == EMPTY:  # 빈공간이라면 더 깊이 탐색한다.
            return dfs(dy, dx, type)
        else:
            if table[dy][dx] == STUDENT:  # 학생이 발견
                return False
            elif table[dy][dx] == OBSTACLE:  # 장해물이 발견
                return True
            else: # 선생이 발견
                return True


def watch():
    temp1 = [False for _ in range(len(teacher))]
    for n in range(len(teacher)):
        temp2 = [False for _ in range(4)]
        for t in range(4):
            temp2[t] = dfs(teacher[n][0], teacher[n][1], t)  # 상, 하 좌,우 학생이 있는지 확인

        if all(temp2):  # 모든학생이 장해물을 피했음.
            temp1[n] = True
        else:  # 학생들이 선생님한테 걸렸음.
            temp1[n] = False

    if all(temp1):
        return True
    else:
        return False


def solve(idx, depth):
    global flag
    if flag:
        return

    if depth == 3:
        if watch():  # 모든학생이 장해물을 피했음.
            flag = True

        return

    for i in range(idx, N * N):
        y = i // N
        x = i % N
        if table[y][x] == EMPTY:
            table[y][x] = OBSTACLE
            solve(i + 1, depth + 1)
            table[y][x] = EMPTY


flag = False
solve(0, 0)
if flag:
    print("YES")
else:
    print("NO")
