# https://www.acmicpc.net/problem/7576
import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())


tomato = [list(map(int, input().split())) for _ in range(N)]
raped = deque()
raw = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            raw.append((i, j))
        elif tomato[i][j] == 1:
            raped.append((i, j, 0))
            
raw_cnt = len(raw)
if raw_cnt == 0:
    print(0)
else:
    max_day = 0
    while raped:
        y, x, day = raped.popleft()
        
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = dy + y, dx + x
            if N > ny >= 0 and M > nx >= 0 and tomato[ny][nx] == 0:
                tomato[ny][nx] = day + 1
                raw_cnt -= 1
                max_day = max(max_day, day + 1)
                raped.append((ny, nx, day + 1))
    if raw_cnt:
        print(-1)
    else:
        print(max_day)


            