# https://www.acmicpc.net/problem/1600
# 너비우선 탐색 해결
# visited 배열을 통하여 방문점을 등록
import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
horse_moves = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
table = []

for _ in range(H):
    table.append(list(map(int, input().split())))
    
queue = deque([(0, 0, 0, K)])
visited = [[[False] * W for _ in range(H)] for _ in range(K+1)]

def is_range(y, x):
    return H > y >=0 and W > x >=0

is_founed = False
while queue:
    y, x, cost, cnt = queue.popleft()
    
    if y == H-1 and x == W-1:
        is_founed = True
        print(cost)
        break
    
    # 말로 움직인다.
    if cnt > 0:
        for dy, dx in horse_moves:
            ny, nx = y + dy, x + dx
            new_cost = cost + 1
            if is_range(ny, nx) and not visited[cnt-1][ny][nx] and table[ny][nx] == 0:
                visited[cnt-1][ny][nx] = True
                queue.append((ny, nx, new_cost, cnt-1))
                
    # 기본으로 움직인다.
    for dy, dx in moves:
        ny, nx = y + dy, x + dx
        new_cost = cost + 1
        if is_range(ny, nx) and not visited[cnt][ny][nx] and table[ny][nx] == 0:
            visited[cnt][ny][nx] = True
            queue.append((ny, nx, new_cost, cnt))
    
if not is_founed:
    print(-1)