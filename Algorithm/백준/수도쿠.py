# https://www.acmicpc.net/problem/2239
import sys
input = sys.stdin.readline
graph = [list(input().strip()) for _ in range(9)]

def check(i, j, num):    
    for k in range(9):
        if graph[k][j] == num or graph[i][k] == num:
            return False
        
    y = i // 3 * 3
    x = j // 3 * 3
    for dy in range(3):
        for dx in range(3):
            if graph[y + dy][x + dx] == num:
                return False
        
    return True

def sudoku(idx):
    if idx == 81:
        for g in graph:
            temp = ''.join(s for s in g)
            print(temp)
            
        exit()
        return True
    
    y = idx // 9
    x = idx % 9
    if graph[y][x] != '0':
        sudoku(idx+1)
    else:
        for num in range(1, 10):
            if check(y, x, str(num)):
                graph[y][x] = str(num)
                if sudoku(idx+1):
                    return True
                graph[y][x] = '0'
                
    return False

sudoku(0)