# https://www.acmicpc.net/problem/1113
# 4*4 + 4*8 = 16 + 32 = 48
# 작은 땅부터 채워 나아간다.
# 1, 2, 3, 4, 5, 6, 7 ...

# 주변에 땅이없고, 자신보다 큰 값이 하나이상있고, 나머지 주변이 자신보다 같거나 클경우 그룹을 만든다.
# 탐색을 하면서 자기자신보다 가장 가까운 높은애만큼 물을 채운다.

# 다시 그룹을 찾는다.
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

pool = [list(str(input().strip())) for _ in range(N)]

ans = 0

def is_land(y, x):
    return 0 > y or y >= N or 0 > x or x >= M

def near_small(y, x, n):
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny, nx = y +dy, x + dx
        if not is_land(ny, nx):
            if n > int(pool[ny][nx]):
                return True
        
    return False

for n in range(1, 10):
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if int(pool[i][j]) == n:
                visited[i][j] = True
                group = []
                queue = deque()
                group.append((i, j))
                queue.append((i, j))
                
                depth = 10
                
                while queue:
                    y, x = queue.popleft()
                    if int(pool[y][x]) != n:
                        depth = min(int(pool[y][x]), depth)
                    
                    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ny, nx = y + dy, x + dx
                        
                        if is_land(ny, nx): # 땅을 만낫을경우
                            group = []
                            break
                        
                        if int(pool[ny][nx]) == n and not visited[ny][nx]:
                            visited[ny][nx] = True
                        
                            if near_small(ny, nx, n):
                                group = []
                                break
                            
                            queue.append((ny, nx))
                            group.append((ny, nx))
                            
                                
                print(group, depth)
                for y, x in group:
                    diff = depth - int(pool[y][x])
                    ans += diff
                    pool[y][x] = str(int(pool[y][x]) + diff)

print(ans)