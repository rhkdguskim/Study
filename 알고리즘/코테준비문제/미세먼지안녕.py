# https://www.acmicpc.net/problem/17144
# 미세먼지의 확산 R*C 시간복잡도 ( 반복문으로 업데이트 테이블 생성후 업데이트 )
# 공기청청기의 동작 R*C보다 작다. ( BFS로 문제해결 )
from collections import deque
from pprint import pprint
moves = ((0,1), (1,0), (-1,0), (0,-1))
R, C, T = map(int, input().split())

graph = []

for _ in range(R):
    graph.append(list(map(int, input().split())))


def spreadDust(graph):
    table = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j] and graph[i][j] != -1:
                sum = 0
                for dy, dx in moves:
                    ny, nx = dy+i, dx+j
                    if R > ny >= 0 and C > nx >=0 and graph[ny][nx] != -1:
                        cost = graph[i][j] // 5
                        table[ny][nx] += cost # 확산시킨다.
                        sum += cost
                        
                table[i][j] -= sum # 확산시킨 값을 뺀다.
                
    for i in range(R):
        for j in range(C):
            graph[i][j] += table[i][j]

def findCleanMachine(graph):
    machine = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] == -1:
                machine.append(i)
                
    return machine[0], machine[1]

def cleanDust(y1, y2):
    # 위쪽 y1
    for i in range(y1-2, -1, -1):
        graph[i+1][0] = graph[i][0]
            
    for i in range(1, C):
        graph[0][i-1] = graph[0][i]
    
    
    for i in range(1, y1+1):
        graph[i-1][C-1] = graph[i][C-1]
            
        
    for i in range(C-1, 0, -1):
        if graph[y1][i-1] == -1:
            graph[y1][i] = 0
        else:
            graph[y1][i] = graph[y1][i-1]
        
    # 아래쪽 y2
    for i in range(y2+2, R-1):
        graph[i-1][0] = graph[i][0]
            
    for i in range(1, C):
        graph[R-1][i-1] = graph[R-1][i]
    
    for i in range(R-2, y2-1, -1):
        graph[i+1][C-1] = graph[i][C-1] 
        
    for i in range(C-1, 0, -1):
        if graph[y2][i-1] == -1:
            graph[y2][i] = 0
        else:
            graph[y2][i] = graph[y2][i-1]
    
y1, y2 = findCleanMachine(graph)

for _ in range(T):
    spreadDust(graph)
    cleanDust(y1, y2)
    
sum = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] != -1:
            sum += graph[i][j]

print(sum)
    