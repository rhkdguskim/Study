# https://www.acmicpc.net/problem/19237

# 1. 인접한 냄새가 없는 칸의 방향을 잡는다.
# 2. 자신의 냄새가 있는 칸으로 방향을 잡는다.
# 3. 만약 여러개일경우, 

# 모든상어가 이동한후 여러마리의 상어가 남아있다면 가장 작은 상어를 제외하고 격자 밖으로 나간다.
# 위, 아래, 왼, 우
import sys
from collections import defaultdict
input = sys.stdin.readline


N, M, k = map(int, input().split())

table = []
shark = []
smell = [[[0, 0] for _ in range(N)] for _ in range(N)]
shark_priority = [[] for _ in range(M)]

for i in range(N):
    temp = list(map(int ,input().split()))
    for j in range(N):
        if temp[j] != 0:
            shark.append([temp[j]-1, i, j])
            
shark.sort(key=lambda x:x[0])
            
shark_dir = list(map(int, input().split()))

for i in range(M):
    for _ in range(4):
        shark_priority[i].append(list(map(int, input().split())))
        

def check_shark(y, x, idx):
    for i, ny, nx in shark:
        if i != idx:
            if ny == y and nx == x:
                if i > idx:
                    shark.pop(i)
                else:
                    shark.pop(idx)

def find_dir(y, x, dir, shark_idx):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 빈칸이 있는경우를 찾는다.
    for d, (dy, dx) in enumerate(moves):
        ny, nx = dy + y, dx + x
        if N > ny >=0 and N > nx >= 0 and smell[ny][nx][0] == 0:
            return ny, nx, d    
    
    # 빈칸이 없다면 우선순위에 따라서 찾는다.
    priority = shark_priority[shark_idx][dir]
    for d in priority:
        dy, dx = moves[d][0], moves[d][1]
        ny, nx = dy + y, dx + x
        if N > ny >=0 and N > nx >=0 and smell[ny][nx][0] == shark:
            return ny, nx, d
        
def smell_remove():
    for i in range(N):
        for j in range(N):
            if smell[i][j][1] > 1:
                smell[i][j][1] -= 1
                
def make_smell(shark):
    for i, y, x in shark:
        smell[y][x][0] = i
        smell[y][x][1] = k
        
time = 0
while True:
    if len(shark) == 1:
        break
    time += 1
    
    target_shark = []
    
    for i, y, x in shark:
        dir = shark_dir[i]
        target_shark.append(find_dir(y, x, dir, i))
    
    for i, (y, x, dir) in enumerate(target_shark):
        shark_dir[i] = dir
        shark[i][1] = y
        shark[i][2] = x
    
    smell_remove()
    make_smell(shark)
    
    
    
print(time)
    