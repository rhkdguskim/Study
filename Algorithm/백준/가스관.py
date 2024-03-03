# https://www.acmicpc.net/problem/2931
import sys
input = sys.stdin.readline
from collections import deque

pipe_type = ['|','-','+','1','2','3','4']
moves = [[(1, 0), (-1, 0)],                     # |
         [(0, 1), (0, -1)],                     # -
         [(1, 0), (0, 1), (-1, 0), (0, -1)],    # +
         [(1, 0), (0, 1)],                      # 1
         [(0, 1), (-1, 0)],                     # 2
         [(0, -1), (-1, 0)],                    # 3
         [(1, 0), (0, -1)]]                     # 4

for i in range(len(moves)):
    moves[i].sort()

corrent_pipe = {}
corrent_pipe[(1, 0)] = ['|', '+', '2', '3']
corrent_pipe[(0, 1)] = ['-', '+', '3', '4']
corrent_pipe[(-1, 0)] = ['|', '+', '1', '4']
corrent_pipe[(0, -1)] = ['-', '+', '1', '2']

# LEFT, RIGHT, UP, DOWN
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def is_range(y, x):
    return R > y >= 0 and C > x >=0

R, C = map(int, input().split())
table = []
queue = deque()
visited = [[False for _ in range(C)] for _ in range(R)]
to_add_pipe = []
for i in range(R):
    temp = list(str(input().strip()))
    for j in range(len(temp)):
        if temp[j] == 'M' or temp[j] == 'Z':
            queue.append((i, j))
            visited[i][j] = True
    table.append(temp)
    
while queue:
    y, x = queue.popleft()
    if table[y][x] == 'M' or table[y][x] == 'Z':
        for dy, dx in direction:
            ny, nx = dy + y, dx + x
            # M과 Z가 왔을때는 파이프로 이동시킨다.
            if is_range(ny, nx) and table[ny][nx] != '.' and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))
    else:
        # 해당파이프로 움직일 수 있는 경우 선택
        idx = pipe_type.index(table[y][x])
        for dy, dx in moves[idx]:
            ny, nx = dy + y, dx + x
            if is_range(ny, nx) and not visited[ny][nx]:
                visited[ny][nx] = True
                # 만약 빈칸이라면
                if table[ny][nx] == '.':
                    to_add_pipe.append((ny, nx))
                else:
                    queue.append((ny, nx))
                    
for y, x in to_add_pipe:
    v = []
    for dy, dx in direction:
        ny, nx = dy + y, dx + x
        if is_range(ny, nx) and table[ny][nx] in corrent_pipe[(dy, dx)]:
            v.append((dy, dx))
            
    v.sort()
    idx = moves.index(v)
    print(y+1, x+1, pipe_type[idx])