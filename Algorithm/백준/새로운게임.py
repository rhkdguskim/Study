# https://www.acmicpc.net/problem/17837
# 체스말은 (위치, 방향, 자식) 을 가지고 있는다.
# table은 딕셔너리형태로 현재위치에 누가 있는지 알아야한다.
# 채스말을 하나씩 순회하면서 문제를 해결하자

import sys
from collections import defaultdict
moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
WHITE = 0
RED = 1
BLUE = 2

input = sys.stdin.readline
N, K = map(int, input().split())

hourse_table = defaultdict(list)
hourse = [[[0, 0], 0, 0] for _ in range(K)]

table = [list(map(int, input().split())) for _ in range(N)]

for i in range(K):
    y, x, d = map(int, input().split())
    y -= 1
    x -= 1
    d -= 1
    
    hourse[i][0] = [y, x]
    hourse[i][1] = d
    hourse[i][2] = 0
    hourse_table[(y, x)].append(i)
    
def is_range(y, x):
    return N > y >=0 and N > x >=0

def change_direction(dir):
    if dir == 0:
        return 1
    
    if dir == 1:
        return 0
    
    if dir == 2:
        return 3
    
    if dir == 4:
        return 3
    
def move(hourse):
    pos, direction, h = hourse
    y, x = pos[0], pos[1]
    dy, dx = move[direction]
    ny, nx = dy + y, dx + x
    if is_range(ny, nx):
        if table[ny][nx] == WHITE:
            for child in hourse_table[(y, x)][h:]:
                hourse_table[(ny, nx)].append(child)
                
            hourse_table[(y, x)] = hourse_table[(y, x)][:h]
        elif table[ny][nx] == RED:
            for child in reversed(hourse_table[(y, x)][h:]):
                hourse_table[(ny, nx)].append(child)
                
            hourse_table[(y, x)] = hourse_table[(y, x)][:h]
        elif table[ny][nx] == BLUE:
            direction = change_direction(direction)
            dy, dx = move[direction]
            ny, nx = dy + y, dx + x
            if is_range(ny, nx):
                if table[ny][nx] != BLUE:
                    y, x = ny, nx
    
    return y, x, direction, h

def popchild(i):
    y, x = hourse[i][0]
    hourse_table
    
    
while True:
    for i in range(K):
        move(hourse[i])
        