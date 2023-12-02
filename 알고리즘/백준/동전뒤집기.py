# https://www.acmicpc.net/problem/1285
# 뒷면이 위로 향하는 동전의 개수를 최소하 하려고한다.
# 동전의 최소 개수를 구하는 프로그램을 작성하라.
# 열이나 행을 탐색햇을때, 뒷면이 더 많으면 무조건 뒤집어야한다.
# 행 탐색 -> 열탐색
# 열탐색 -> 행탐색
# 더 많이 뒤집은 애를 뒤집는다.

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().strip()) for _ in range(N)]

def toggle(y, x):
    if graph[y][x] == 'T':
        graph[y][x] = 'H'
    else:
        graph[y][x] = 'T'
    

def min_t_cnt():
    # 행을 확인한다.
    row_visited = []
    row_cnt = 0
    for i in range(N):
        t_cnt = 0
        h_cnt = 0
        for j in range(N):
            if graph[i][j] == 'H':
                h_cnt += 1
            else:
                t_cnt += 1
        
        if t_cnt > h_cnt:
            for k in range(N):
                if graph[i][k] == 'T':
                    row_cnt += 1
                row_visited.append((i,k))
                
    # 열을 확인한다.
    col_visited = []
    col_cnt = 0
    for j in range(N):
        t_cnt = 0
        h_cnt = 0
        for i in range(N):
            if graph[i][j] == 'H':
                h_cnt += 1
            else:
                t_cnt += 1
        if t_cnt > h_cnt: # 뒷면이 더 많은경우 뒤집는다.
            for k in range(N):
                if graph[k][j] == 'T':
                    col_cnt += 1
                col_visited.append((k,j))
                
    if col_cnt > row_cnt:
        for v_i, v_j in col_visited:
            toggle(v_i, v_j)
    else:
        for v_i, v_j in row_visited:
            toggle(v_i, v_j)
    
    total = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'T':
                total += 1
    
    return total

t_cnt = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            t_cnt += 1
            
prev_t_cnt = t_cnt
while True:
    new_t_cnt = min_t_cnt()
    if new_t_cnt != prev_t_cnt:
        prev_t_cnt = new_t_cnt
    else:
        break
        
print(prev_t_cnt)
