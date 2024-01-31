# https://www.acmicpc.net/problem/1113

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

pool = [list(str(input().strip())) for _ in range(N)]

ans = 0

def find_min(queue, n):
    min_value = 10
    for y, x in queue:
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = dy + y, dx + x
            if N > ny >=0 and M > nx >=0 and int(pool[ny][nx]) != n:
                min_value = min(min_value, int(pool[ny][nx]))
    
    return min_value

for n in range(1, 10):
    visited = [[False for _ in range(M)] for _ in range(N)]
    
    # 외각에 있는 애들 다 방문처리 하기
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0 or i == N-1 or j == M-1:
                if int(pool[i][j]) == n and not visited[i][j]:
                    visited[i][j] = True
                    queue = deque()
                    queue.append((i, j))
                    
                    while queue:
                        y, x = queue.popleft()
                        
                        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            ny, nx = dy + y, dx + x
                            if N > ny >=0 and M > nx >= 0 and not visited[ny][nx] and int(pool[ny][nx]) == n:
                                visited[ny][nx] = True
                                queue.append((ny, nx))
    
    for i in range(N):
        for j in range(M):
            if int(pool[i][j]) == n and not visited[i][j]:
                visited[i][j] = True
                queue = deque()
                queue.append((i, j))
                group = []
                group.append((i, j))
                
                while queue:
                    y, x = queue.popleft()
                    
                    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        ny, nx = dy + y, dx + x
                        if N > ny >=0 and M > nx >= 0 and not visited[ny][nx] and int(pool[ny][nx]) == n:
                            visited[ny][nx] = True
                            queue.append((ny, nx))
                            group.append((ny, nx))
                
                
                min_value = find_min(group, n)
                # print(group, min_value)
                if min_value > n:
                    for y, x in group:
                        ans += (min_value - n)
                        pool[y][x] = str(min_value)
    
    # for p in pool:
    #     print(p)

print(ans)
