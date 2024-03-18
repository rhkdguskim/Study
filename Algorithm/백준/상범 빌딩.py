# https://www.acmicpc.net/problem/6593
import sys
from collections import deque
input = sys.stdin.readline
moves = [(0, 0, 1), (0, 1, 0), (1, 0, 0),
             (0, 0, -1), (0, -1, 0), (-1, 0, 0)]

def is_range(i, j, k):
    return L > i >=0 and R > j >=0 and C > k >=0

while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    
    s_h, s_y, s_x = 0, 0, 0
    e_h, e_y, e_x = 0, 0, 0
    table = [[] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            temp = list(str(input().strip()))
            for k in range(C):
                if temp[k] == 'S':
                    s_h, s_y, s_x = i, j, k
                elif temp[k] == 'E':
                    e_h, e_y, e_x = i, j, k
                    
            table[i].append(temp)
        input()
    
    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    visited[s_h][s_y][s_x] = True
    queue = deque()
    queue.append((s_h, s_y, s_x, 0))
    
    is_ended = False
    while queue:
        h, y, x, cost = queue.popleft()
        if h == e_h and y == e_y and x == e_x:
            print("Escaped in {} minute(s).".format(cost))
            is_ended = True
            break
        
        for dh, dy, dx in moves:
            nh, ny, nx = dh + h, dy + y, dx + x
            if is_range(nh, ny, nx):
                v = not visited[nh][ny][nx]
                t = table[nh][ny][nx] == '.' or table[nh][ny][nx] == 'E'
                if v and t:
                    visited[nh][ny][nx] = True
                    queue.append((nh, ny, nx, cost + 1))
    
    if not is_ended:
        print("Trapped!")
        
    # for v in visited:
    #     for k in v:
    #         print(k)
            
    #     print()