# https://www.acmicpc.net/problem/19238
# 손님을 목적지로 데려다 줄때마다 연료가 충전됨.
# 연료가 바닥나면 그날의 업무가 끝난다.
# M명의 승객을 태우는게 목표이다.

# 승객 고르는 방법
# 현재위치에서 가장 최단거리가 짧은 승객을 고른다.
# 그런승객이 여러명이면, 그중 행번호, 열번호 순으로 작은 승객을 고른다.

# 택시 이동법
# 택시는 항상 최단거리로 이동한다.
# 이동할때마다 연로를 1만큼 소모된다.
# 승객을 목적지로 성공적으로 이동시키면, 승객을 태워 이동하면서 소모한 연료의 양이 2배가 충전된다.
# 이동하는 도중 바닥나면 이동에 실패하고 업무가 끝난다.
# 이동시킨 동시에 연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.

# 모든 승객을 목적지까지 나른뒤, 남은 연료의 양을 출력한다.
# 만약 실패한다면 -1을 출력한다.
from collections import deque
import sys
input = sys.stdin.readline

N, M, T = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]
passenger = set()
destination = {}
    

start_x, start_y = map(int, input().split())

for _ in range(M):
    s_y, s_x, d_y, d_x = map(int, input().split())
    passenger.add((s_y-1, s_x-1))
    destination[(s_y-1, s_x-1)] = (d_y-1, d_x-1)
    
    
# 현재 택시 위치에서, passenger까지의 최단경로를 구한다.
def min_distacne(s_y, s_x, passenger):
    queue = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[s_y][s_x] = True
    queue.append((s_y, s_x, 0))
    dest = []
    while queue:
        y, x , cost = queue.popleft()
        if (y, x) in passenger:
            dest.append((y, x, cost))
        
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = dy + y, dx + x
            if N > ny >=0 and N > nx >=0 and table[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, cost + 1))
        
    if not dest:
        return None
    else:
        dest.sort(key=lambda x:(x[2], x[0], x[1]))
        return dest[0]

def move_passenger(s_y, s_x, t_y, t_x):
    queue = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[s_y][s_x] = True
    queue.append((s_y, s_x, 0))
    while queue:
        y, x , cost = queue.popleft()
        if y == t_y and x == t_x:
            return (y, x, cost)
        
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = dy + y, dx + x
            if N > ny >=0 and N > nx >=0 and table[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx, cost + 1))
                
    return None

start_x -= 1
start_y -= 1

while passenger and T:
    t_passenger = min_distacne(start_x, start_y, passenger)
    if t_passenger is None:
        #print("손님없음")
        break
    
    T -= t_passenger[2]
    
    if T <= 0:
        #print("기름없음")
        break
    
    #print("이동후 기름", T)
    
    dest_y, dest_x = destination[(t_passenger[0], t_passenger[1])]
    
    moved = move_passenger(t_passenger[0], t_passenger[1], dest_y, dest_x)
    
    if moved is None:
        #print("손님을 옮길 수 없음.")
        break
    
    start_x, start_y = moved[:2]
    T -= moved[2]
    
    # 기름이 0이상일경우는 승객을 옮겼음.
    if T >= 0:
        passenger.remove((t_passenger[0], t_passenger[1]))
        T += (moved[2]) * 2
    
    #print("승객후 기름", T)

if passenger:
    print(-1)
else:
    print(T)