# https://www.acmicpc.net/problem/7576
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def bfs(raped):
    new_raped = set()
    
    for y, x in raped:
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = dy + y, dx + x
            if N > ny >= 0 and M > nx >= 0 and tomato[ny][nx] == 0:
                tomato[ny][nx] = 1
                new_raped.add((ny, nx))
    
    return new_raped

tomato = [list(map(int, input().split())) for _ in range(N)]
raped = set()
raw = []
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            raw.append((i, j))
        elif tomato[i][j] == 1:
            raped.add((i, j))

day = 0
raw_cnt = len(raw)

if len(raped) == 0:
    print(0)
else:
    while True:
        new_raped = bfs(raped)
        if len(new_raped) == 0:
            break
        
        day += 1
        raw_cnt -= len(new_raped)
        raped |= new_raped
    
    if raw_cnt == 0:
        print(day)
    else:
        print(-1)