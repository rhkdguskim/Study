# https://www.acmicpc.net/problem/17837
# 체스말은 (위치, 방향, 자식) 을 가지고 있는다.
# table은 딕셔너리형태로 현재위치에 누가 있는지 알아야한다.
# 채스말을 하나씩 순회하면서 문제를 해결하자

import sys
moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
WHITE = 0
RED = 1
BLUE = 2

input = sys.stdin.readline
N, K = map(int, input().split())

chess = [[[] for _ in range(N)] for _ in range(N)]
horse = []
table = [list(map(int, input().split())) for _ in range(N)]

def chage_direction(dir):
    if dir in [0, 2]:
        return dir + 1

    if dir in [1, 3]:
        return dir - 1

def solve(i):
    y, x , dir = horse[i]
    dy, dx = moves[dir]
    ny, nx = dy + y, dx + x
    if nx >= N or nx < 0 or ny >=N or ny < 0 or table[ny][nx] == BLUE:
        dir = chage_direction(dir)
        horse[i][2] = dir
        dy, dx = moves[dir]
        ny, nx = dy + y, dx + x
        if nx >= N or nx < 0 or ny >=N or ny < 0 or table[ny][nx] == BLUE:
            return False
    
    horse_up = []
    for idx, num in enumerate(chess[y][x]):
        if num == i:
            horse_up.extend(chess[y][x][idx:])
            chess[y][x] = chess[y][x][:idx]
            break
    
    if table[ny][nx] == RED:
        horse_up = horse_up[-1::-1]
    
    for num in horse_up:
        horse[num][0], horse[num][1] = ny, nx
        chess[ny][nx].append(num)
    
    if len(chess[ny][nx]) >= 4:
        return True
    else:
        return False
    
    
for i in range(K):
    y, x, d = map(int, input().split())
    y -= 1
    x -= 1
    d -= 1
    chess[y][x].append(i)
    horse.append([y, x, d])

is_finished = False
time = 0
while True:
    if time > 1000:
        print(-1)
        break
    
    for i in range(K):
        if solve(i):
            is_finished = True
            break
        
    time += 1    
    if is_finished:
        print(time)
        break
    
