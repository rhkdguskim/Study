# https://www.acmicpc.net/problem/4574
import sys
input = sys.stdin.readline

def get_pos(LU):
    y, x = ord(LU[0]) - ord('A'), int(LU[1])-1
    return y, x

def is_range(y, x):
    return 8 >= y >=0 and 8 >= x >=0

def change_pos(y, x):
    x += 1
    if x == 9:
        x = 0
        y += 1
    return y, x

def check_height_width(y1, x1, y2, x2, num1, num2):
    for i in range(9):
        if x1 != i:
            if table[y1][i] == num1:
                return True
        if y1 != i:
            if table[i][x1] == num1:
                return True
        
        if x2 != i:
            if table[y2][i] == num2:
                return True
        if y2 != i:
            if table[i][x2] == num2:
                return True
    return False

def check_cross(y, x, num):
    for i in range((y // 3) * 3, (y // 3) * 3 + 3):
        for j in range((x // 3) * 3, (x // 3) * 3 + 3):
            if table[i][j] == num and i != y and j != x:
                return True
            
    return False

def check(y1, x1, y2, x2, num1, num2):
    if check_height_width(y1, x1, y2, x2, num1, num2):
        return False
    
    if check_cross(y1, x1, num1) or check_cross(y2, x2, num2):
        return False
        
    return True

def solve(i,j, visited):
    global cnt
    if i == 8 and j == 8:
        print("Puzzle", cnt)
        for i in range(9):
            for j in range(9):
                print(table[i][j], end='')
            print()
        return True
    
    if table[i][j] != 0:
        new_i, new_j = change_pos(i, j)
        return solve(new_i, new_j, visited)
    
    
    for dy, dx in [(0, 1), (1, 0)]: # 세로로 넣어보기, 가로로 넣어보기
        ny, nx = i + dy, j + dx
        if not is_range(ny, nx) or table[ny][nx] != 0:
            continue
        
        for num1 in range(1, 10):
            for num2 in range(1, 10):
                if not visited[num1][num2] and num1 != num2:
                    if check(i, j, ny, nx, num1, num2):
                        visited[num1][num2] = True
                        visited[num2][num1] = True
                        table[i][j] = num1
                        table[ny][nx] = num2
                        
                        new_i, new_j = change_pos(i, j)
                        if solve(new_i, new_j, visited):
                            return True
                        
                        table[i][j] = 0
                        table[ny][nx] = 0
                        visited[num1][num2] = False
                        visited[num2][num1] = False

cnt = 1
while True:
    N = int(input().strip())
    table = [[0 for _ in range(9)] for _ in range(9)]
    visited = [[False for _ in range(10)] for _ in range(10)]
    if N == 0:
        break
    
    for _ in range(N):
        U, LU, V, LV = map(str, input().split())
        num1 = int(U)
        y1, x1 = get_pos(LU)
        num2 = int(V)
        y2, x2 = get_pos(LV)
        table[y1][x1] = num1
        table[y2][x2] = num2
        visited[num1][num2] = True
        visited[num2][num1] = True
    
    for num, pos in enumerate(list(map(str, input().split()))):
        y, x = get_pos(pos)
        table[y][x] = num+1
    
    solve(0, 0, visited)
    cnt += 1

