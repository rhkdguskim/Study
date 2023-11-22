# https://www.acmicpc.net/problem/1194

from collections import deque
N, M = map(int, input().split()) # 세로, 가로
move = [(0,1), (0,-1), (1,0), (-1,0)]
keys = ('a', 'b', 'c', 'd', 'e', 'f')
doors =  ('A', 'B', 'C', 'D', 'E', 'F')
start = []
graph = []
for i in range(N):
    char = input()
    for j in range(M):
        if char[j] == '0':
            start.append(i)
            start.append(j)
    graph.append(list(map(str, char)))


def bfs():
    visited = [ [[0 for _ in range( (1<<6))] for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append([start[0], start[1], 0])
    graph[start[0]][start[1]] = '.'
    visited[start[0]][start[1]][0] = 0
    while queue:
        i , j, key = queue.popleft()
        for dy, dx in move:
            ny, nx = i + dy, j + dx
            newkey = key
            if N > ny >= 0 and M > nx >= 0 and not visited[ny][nx][key] and graph[ny][nx] != '#':
                if graph[ny][nx] in keys: # 키라면
                    newkey |= 1 << keys.index(graph[ny][nx])
                        
                elif graph[ny][nx] in doors: # 문이라면
                    if not (key & 1 << doors.index(graph[ny][nx])): # 키가 없다면
                       continue
                       
                elif graph[ny][nx] == '1' : # 1이라면
                    return visited[i][j][key] + 1
                
                visited[ny][nx][newkey] = visited[i][j][key] + 1
                queue.append([ny, nx, newkey])
                            
    return None
                
result = bfs()
if result == None:
    print(-1)
else:
    print(result)