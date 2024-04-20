# https://www.acmicpc.net/problem/2933
import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
table = [list(str(input().strip())) for _ in range(R)]
N = int(input())
attack_list = list(map(int, input().split()))

LEFT = 0
RIGHT = 1

def change_direction(direction):
    if direction == LEFT:
        return RIGHT
    else:
        return LEFT

def attack(h, direction):
    if direction == LEFT:
        for i in range(C):
            if table[h][i] == 'x':
                table[h][i] = '.'
                return
    else:
        for i in range(C-1, -1 ,-1):
            if table[h][i] == 'x':
                table[h][i] = '.'
                return

def is_land(y, x):
    return y == R-1

def is_range(y, x):
    return R > y >=0 and C > x >=0

def find_min_height(queue):
    min_height = R
    for y, x in queue:
        cnt = 1
        for i in range(y+2, R):
            if (i, x) not in queue:
                if table[i][x] == 'x':
                    min_height = min(min_height, cnt)
                    break
            cnt += 1
            
        min_height = min(min_height, cnt)
    return min_height

def move(group):
    queue = deque()
    for q in group:
        queue.append((q[0], q[1], 0))
        table[q[0]][q[1]] = '.'
        
    while queue:
        y, x, cost = queue.popleft()
        
        if y == R-1 or table[y+1][x] == 'x':
            for n_y, n_x in group:
                table[n_y + cost][n_x] = 'x'
            break
                
        queue.append((y+1, x, cost + 1))

def move_down():
    # 바닥까지 혹은 크리스탈까지의 최소 거리를 찾아서 내린다.
    visited = [[False for _ in range(C)] for _ in range(R)]
    groups = []
    for i in range(R):
        for j in range(C):
            if table[i][j] == 'x' and not visited[i][j]:
                land_flag = False
                queue = deque()
                queue.append((i, j))
                group = []
                group.append((i, j))
                visited[i][j] = True
                
                while queue:
                    y, x = queue.popleft()
                    if is_land(y, x):
                        land_flag = True
                    
                    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ny, nx = dy + y, dx + x
                        if is_range(ny, nx) and not visited[ny][nx] and table[ny][nx] == 'x':
                            visited[ny][nx] = True
                            queue.append((ny, nx))
                            group.append((ny, nx))
                            
                if not land_flag:
                    groups.append(group)
                    
    for group in groups:
        move(group)
                    

direction = LEFT
for i in range(N):
    attack(R - attack_list[i], direction)
    # print("after attack", (attack_list[i], direction))
    # for t in table:
    #     print(''.join(t))
    
    
    move_down()
    
    # print("after move")
    # for t in table:
    #     print(''.join(t))
    
    direction = change_direction(direction)

for t in table:
    print(''.join(t))