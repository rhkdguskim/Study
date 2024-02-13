# https://www.acmicpc.net/problem/4574
import sys
input = sys.stdin.readline


def update_graph_bystring(num, char):
    i = ord(char[0]) - ord('A')
    j = int(char[1]) - 1
    graph[i][j] = int(num)

def get_pos(y, x):
    i , j = 0, 0
    if 0 <= y < 3:
        i = 0
    elif 3 <= y < 6:
        i = 3
    else :
        i = 6
    
    if 0 <= x < 3:
        j = 0
    elif 3 <= x < 6:
        j = 3
    else :
        j = 6
        
    return i, j
    
def check(y, x, num):
    for i in range(9):
        # 가로 중복 확인
        if i != x:
            if graph[y][i] == num:
                return False
        # 세로 중복 확인    
        if i != y:
            if graph[i][x] == num:
                return False
            
    ny, nx = get_pos(y, x)
    for i in range(3):
        for j in range(3):
            if y != i+ny and x != j+nx:
                if graph[i+ny][j+nx] == num:
                    return False
                
    return True
         
    
    
def sudoku(idx):
    global flag, cnt
    if flag:
        return True
    
    if idx == 81: # BaseCase
        print("Puzzle", end=' ')
        print(cnt)
        for g in graph:
            print(''.join(str(number) for number in g))
        flag = True
        return True
    
    y = idx // 9
    x = idx % 9
    if graph[y][x] != 0:
        return sudoku(idx+1)
    
    for dy, dx in [(1,0), (0,1)]:
        ny, nx = dy + y, dx + x
        if 9 > ny >= 0 and 9 > nx >=0 and graph[ny][nx] == 0:
            for num1 in range(1, 10):
                for num2 in range(1, 10):
                    if num1 == num2 or visited[num1][num2]: continue
                    if check(y, x, num1) and check(ny, nx, num2):
                        graph[y][x] = num1
                        graph[ny][nx] = num2
                        visited[num1][num2] = True
                        visited[num2][num1] = True
                        if sudoku(idx+1): return True
                        graph[y][x] = 0
                        graph[ny][nx] = 0
                        visited[num1][num2] = False
                        visited[num2][num1] = False       
    return False
                
    
cnt = 1
while True:
    N = int(input())
    graph = [[0 for _ in range(9)] for _ in range(9)]
    visited = [[False for _ in range(10)] for _ in range(10)]
    if N == 0:
        break
    
    for _ in range(N):
        U, LU, V, LV = map(str, input().split())
        update_graph_bystring(U, LU)
        update_graph_bystring(V, LV)
        visited[int(U)][int(V)] = True
        visited[int(V)][int(U)] = True
        

    list_char = list(map(str ,input().split()))
    for i in range(len(list_char)):
        update_graph_bystring(i+1, list_char[i])
    
    flag = False
    
    sudoku(0)
    cnt += 1