# https://www.acmicpc.net/problem/5427
import sys
from collections import deque
input = sys.stdin.readline
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())

for _ in range(T):
    w, h = map(int, input().split())
    graph = []
    queue = deque()
    visited = [[False for _ in range(w)] for _ in range(h)]
    
    sungbum = None, None
    for i in range(h):
        temp = list(input().strip())
        for j in range(w):
            if temp[j] != '.':
                visited[i][j] = True
                if temp[j] == "@":
                    sungbum = i, j
                else:
                    queue.append((i ,j, temp[j], 0))

        graph.append(temp)
    
    queue.append((sungbum[0], sungbum[1], "@", 0))
    is_finished = False
    while queue:
        y, x, c, cost = queue.popleft()
        
        for dy, dx in moves:
            ny, nx = dy + y, dx + x
            if is_finished:
                break
            
            # 불일때
            if c == '*' and h > ny >=0 and w > nx >=0 and not visited[ny][nx] and graph[ny][nx] == '.':
                graph[ny][nx] = c
                visited[ny][nx] = True
                queue.append((ny, nx, c, cost))
            
            # 상은이 일때
            if c == '@':
                if h > ny >=0 and w > nx >=0:
                    if graph[ny][nx] == '.' and not visited[ny][nx]:
                        graph[ny][nx] = c
                        visited[ny][nx] = True
                        queue.append((ny, nx, c, cost + 1))
                else:
                    print(cost + 1)
                    is_finished = True
                    break
    if not is_finished:
        print("IMPOSSIBLE")