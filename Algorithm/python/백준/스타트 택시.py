# https://www.acmicpc.net/problem/19238

# 현재위치에서 가장 짧은 승객을 고른다.
    # 그중에 여러명이면 번호가 가장 작은 승객고른다.
# 연로는 한칸 이동할때마다 1만큼 소모되고, 성공적으로 이동시키면 연료 양의 두배가된다.
# 
import sys
from collections import deque
input = sys.stdin.readline

N, M, OIL = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
start_y, start_x = map(int, input().split())
start_y -= 1
start_x -= 1

passenger = dict()
for _ in range(M):
    s_y, s_x, e_y, e_x = map(int, input().split())
    s_y -= 1
    s_x -= 1
    e_y -= 1
    e_x -= 1
    passenger[(s_y, s_x)] = (e_y, e_x)
    
def find_min_passenget(start_y, start_x):
    INF = sys.maxsize
    queue = deque()
    visited = [[False]*N for _ in range(N)]
    queue.append((start_y, start_x, 0))
    visited[start_y][start_x] = True
    mindisance = INF
    end_y, end_x = -1, -1
    while queue:
        y, x, cost = queue.popleft()
        
        if cost > mindisance:
            continue
        
        if (y, x) in passenger:
            if mindisance >= cost:
                if mindisance == cost:
                    if end_y >= y:
                        if end_y == y:
                            if end_x > x:
                                end_y, end_x = y, x
                        else:
                            end_y, end_x = y, x
                        
                else:
                    end_y, end_x = y, x
                    mindisance = cost

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx =  dy + y, dx + x
            if N > ny >= 0 and N > nx >=0 and table[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, cost + 1))

    return end_y, end_x, mindisance

def move(start_y, start_x, end_y, end_x):
    queue = deque()
    visited = [[False]*N for _ in range(N)]
    queue.append((start_y, start_x, 0))
    visited[start_y][start_x] = True
    while queue:
        y, x, cost = queue.popleft()
        if end_y == y and end_x == x:
            return y, x, cost
        
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx =  dy + y, dx + x
            if N > ny >= 0 and N > nx >=0 and table[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, cost + 1))
                
                
    return -1, -1, -1


while True:
    y, x, distance = find_min_passenget(start_y, start_x)
    if y == -1 and x == -1:
        break
    
    OIL -= distance
    if OIL <= 0:
        break
    
    end_y, end_x = passenger[(y, x)]
    
    new_y, new_x, distance2 = move(y, x, end_y, end_x)
    if new_y == -1 and new_x == -1:
        break
    
    OIL -= distance2
    if OIL < 0:
        break
    
    M -= 1
    passenger.pop((y, x))
    start_y, start_x = new_y, new_x
    OIL += (distance2)*2
    

if M:
    print(-1)
else:
    print(OIL)