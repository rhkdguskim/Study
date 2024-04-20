# https://www.acmicpc.net/problem/17143
import sys
input = sys.stdin.readline

UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4

move = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]

R, C, M = map(int, input().split())

sharks = {}

for _ in range(M):
    y, x, s, d, z = map(int, input().split())
    sharks.setdefault((y, x), (s, d, z)) # (r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기

def fish_shark(x):
    y = 1
    cost = 0
    while C >= y:
        if sharks.get((y, x)):
            _, _, cost = sharks.pop((y, x))
            #print("!!! eat shark", y, x)
            break
    
        y += 1
    
    return cost

def change_direction(y, x, direction):
    if y == 1 and direction == UP:
        return DOWN
    
    if y == R and direction == DOWN:
        return UP
                
    if x == 1 and direction == LEFT:
        return RIGHT
            
    if x == C and direction == RIGHT:
        return LEFT

    return direction

def move_shark(sharks):
    new_sharks = {}
    for key in sharks:
        y, x = key
        speed, direction, size = sharks[key]
        
        distance = speed
        while distance:
            direction = change_direction(y, x, direction)
            
            dy, dx = move[direction]
            
            y, x = y + dy, x + dx
            
            distance -= 1
        
        if new_sharks.get((y, x)):
            if size > new_sharks[(y, x)][2]:
                new_sharks[(y, x)] = (speed, direction, size)
        else:
            new_sharks.setdefault((y, x), (speed, direction, size))
    
    return new_sharks

ans = 0
for c in range(1, C+1):
    ans += fish_shark(c)
    # print('before --------')
    
    # for key in sharks:
    #     print(key, end = ' ')
    
    # print()
    sharks = move_shark(sharks)
    
    # print('after--------')
    # for key in sharks:
    #     print(key, end = ' ')
    # print()
    
print(ans)