# https://www.acmicpc.net/problem/20058
import sys
from collections import deque
input = sys.stdin.readline

move = [(0,1), (1,0),(-1,0), (0,-1)]

N, Q = map(int, input().split())
ice = []
for _ in range(2**N):
    ice.append(list(map(int, input().split())))

cmd = list(map(int, input().split()))

def find_max_group():
    visited = [[False for _ in range(2**N)] for _ in range(2**N)]
    ans = 0
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            if ice[i][j] >0 and not visited[i][j]:
                visited[i][j] = True
                queue = deque()
                queue.append((i, j))
                cnt = 1
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in move:
                        ny , nx = dy + y, dx + x
                        if 2**N > ny >=0 and 2**N > nx >=0 and not visited[ny][nx] and ice[ny][nx] > 0:
                            cnt += 1
                            visited[ny][nx] = True
                            queue.append((ny, nx))
                            
            ans = max(ans, cnt)
                            
    return ans
    

def melt():
    temp = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            cnt = 4
            for dy, dx in move:
                ny, nx = dy+i, dx + j
                if 2**N > ny >=0 and 2**N > nx >=0 and ice[ny][nx] > 0:
                    cnt -= 1
            if cnt >= 2:
                temp[i][j] = 1
    
    for i in range(2**N):
        for j in range(2**N):
            if ice[i][j] > 0:
                ice[i][j] -= temp[i][j]
            
            

def rotate(start, end, size):
    temp = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            temp[j][size-1-i] = ice[i+start][j+end]
            
    for i in range(size):
        for j in range(size):
            ice[i+start][j+end] = temp[i][j]
    

def dfs(start, end, size):
    if size == 2**L: # 시계방향으로 회전시킨다.
        rotate(start, end, size)
        return
    
    mid = size // 2
    dfs(start, end, size//2) # 왼쪽 위
    dfs(start + mid, end, size//2) # 왼쪽 아래
    dfs(start, end + mid, size//2) # 오른쪽 위
    dfs(start + mid, end + mid, size//2) # 오른쪽 아래

for i in range(Q):
    L = cmd[i]
    dfs(0, 0, 2**N)
    melt()
    
ans = 0
for ic in ice:
    #print(ic)
    ans += sum(ic)
    
print(ans)
print(find_max_group())