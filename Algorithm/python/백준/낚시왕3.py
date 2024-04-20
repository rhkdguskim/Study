import sys
input = sys.stdin.readline

UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4

dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

R, C, M = map(int, input().split())


table = [[[0] for _ in range(C+1)] for _ in range(R+1)]

def is_range(y, x):
    return R >= y >= 1 and C >= x >=1

def chage_direction(direction):
    if direction == UP:
        return DOWN
    elif direction == DOWN:
        return UP
    elif direction == RIGHT:
        return LEFT
    else:
        return RIGHT

def move(y, x, speed, direction):
    if direction == UP or direction == DOWN:
        speed = speed % ((R-1)*2)
    else:
        speed = speed % ((C-1)*2)
    
    ny, nx = y, x
    
    for _ in range(speed):
        ny += dy[direction]
        nx += dx[direction]
        if is_range(ny, nx):
            continue
        else:
            ny -= dy[direction]
            nx -= dx[direction]
            direction = chage_direction(direction)
            ny += dy[direction]
            nx += dx[direction]
    
    return ny, nx, direction

def move_shark(table):
    new_table = [[[0] for _ in range(C+1)] for _ in range(R+1)]
    for i in range(1, R+1):
        for j in range(1, C+1):
            if len(table[i][j]) >= 2:
                speed, direction, size = table[i][j]
                n_y, n_x, direction = move(i, j, speed, direction)

                if len(new_table[n_y][n_x]) == 1:
                    new_table[n_y][n_x] = [speed, direction, size]
                else:
                    if size > new_table[n_y][n_x][2]:
                        new_table[n_y][n_x] = [speed, direction, size]
                    
    return new_table

def catch_shark(x):
    for i in range(1, R+1):
        if len(table[i][x]) >= 2:
            size = table[i][x][2]
            table[i][x] = [0]
            return size
    
    return 0
    
for _ in range(M):
    y, x, s, d, z = map(int, input().split())
    table[y][x] = [s, d, z] # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기
    
    
ans = 0
for x in range(1, C+1):
    cost = catch_shark(x)
    ans += cost
    table = move_shark(table)

print(ans)
    