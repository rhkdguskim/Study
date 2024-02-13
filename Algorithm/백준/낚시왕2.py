# https://www.acmicpc.net/problem/17143

import copy
import sys
input = sys.stdin.readline

N, M, S = map(int, input().split())
arr = [[0] * (M+1) for _ in range(N+1)]
for _ in range(S):
    n, m, speed, direction, big = map(int, input().split())
    arr[n][m] = (speed, direction, big)
shark_move = [[], [-1, 0], [1, 0], [0, 1], [0, -1]]


def fishing(now):
    global result
    for i in range(1, N+1):
        if arr[i][now] != 0:
            result += arr[i][now][2]
            arr[i][now] = 0
            break


def move_shark():
    global arr
    temp = [[0]*(M+1)for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j] != 0:
                speed, dir, big = arr[i][j]
                n, m, dir = moveOne(i, j, speed, dir)
                if temp[n][m] == 0:
                    temp[n][m] = (speed, dir, big)
                else:
                    if temp[n][m][2] < arr[i][j][2]:
                        temp[n][m] = (speed, dir, big)
    arr = copy.deepcopy(temp)


def moveOne(i, j, speed, dir):
    if dir == 1 or dir == 2:
        speed = speed % ((N-1)*2)
    else:
        speed = speed % ((M-1)*2)
    n, m = i, j
    for _ in range(speed):
        n += shark_move[dir][0]
        m += shark_move[dir][1]
        if 0 < n <= N and 0 < m <= M:
            continue
        else:
            n -= shark_move[dir][0]
            m -= shark_move[dir][1]
            dir = change_dir(dir)
            n += shark_move[dir][0]
            m += shark_move[dir][1]
    return n, m, dir


def change_dir(dir):
    if dir == 1:
        return 2
    elif dir == 2:
        return 1
    elif dir == 3:
        return 4
    else:
        return 3


result = 0
for i in range(1, M+1):
    fishing(i)
    move_shark()
print(result)