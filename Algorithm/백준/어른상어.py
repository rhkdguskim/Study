# https://www.acmicpc.net/problem/19237

# 상어는 1이상 M이하 자연수 번호가 붙어있다.
# 1의 번호를 가진 어른 상어는 가장 강력해서 모두를 쫓아 낼 수 있다.

# 1. 인접한 냄새가 없는 칸의 방향을 잡는다.
# 2. 자신의 냄새가 있는 칸으로 방향을 잡는다.
# 3. 만약 여러개일경우, 
# 모든 상어가 동시에 움직인다. 자신의 냄새를 그 칸에 뿌린다.
# 인접한 칸중 아무 냄새가 없는 방향으로 잡는다.
# 그런칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
# 가능한 칸이 여러개 일 수 있는데, 특정 우선순위에따라서 칸을 선택한다.

# 위, 아래, 왼, 우
import sys
from collections import defaultdict
input = sys.stdin.readline

N, M, k = map(int, input().split())

table = []
shark = []
smell = [[[-1, 0] for _ in range(N)] for _ in range(N)]
shark_priority = [[] for _ in range(M)]

for i in range(N):
    temp = list(map(int ,input().split()))
    for j in range(N):
        if temp[j] != 0:
            shark.append([temp[j]-1, i, j])
            
shark.sort(key=lambda x:x[0])
            
shark_dir = list(d-1 for d in list(map(int, input().split())))

for i in range(M):
    for _ in range(4):
        shark_priority[i].append(list(d-1 for d in list(map(int, input().split()))))

def find_dir(y, x, dir, shark_idx):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    priority = shark_priority[shark_idx][dir]
    
    # 빈칸이 있는경우를 찾는다.
    for d in priority:
        dy, dx = moves[d][0], moves[d][1]
        ny, nx = dy + y, dx + x
        if N > ny >=0 and N > nx >= 0 and smell[ny][nx][0] == -1:
            return ny, nx, d
    
    # 빈칸이 없다면 우선순위에 따라서 찾는다.
    for d in priority:
        dy, dx = moves[d][0], moves[d][1]
        ny, nx = dy + y, dx + x
        if N > ny >=0 and N > nx >=0 and smell[ny][nx][0] == shark_idx:
            return ny, nx, d
    
    
def smell_remove():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] >= 1:
                smell[i][j][1] -= 1
            
            if smell[i][j][1] == 0:
                smell[i][j][0] = -1
                
def make_smell(shark):
    for i, y, x in shark:
        smell[y][x][0] = i
        smell[y][x][1] = k
        
time = 0
while True:
    if time > 1000:
        break
    
    if len(shark) == 1:
        break
    time += 1
    
    target_shark = []
    
    for i, y, x in shark:
        dir = shark_dir[i]
        ny, nx, n_dir = find_dir(y, x, dir, i)
        target_shark.append((i, ny, nx))
        shark_dir[i] = n_dir
        
    new_shark = []
    target_shark.sort(key=lambda x:x[0])
    visited = set()
    for idx, y, x in target_shark:
        if (y, x) not in visited:
            visited.add((y, x))
            new_shark.append((idx, y, x))
    
    
    make_smell(shark)
    smell_remove()
    shark = new_shark

if time > 1000:
    print(-1)
else:
    print(time)
    