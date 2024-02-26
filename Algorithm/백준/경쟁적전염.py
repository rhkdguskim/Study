# https://www.acmicpc.net/problem/18405
import sys
input = sys.stdin.readline


N, K = map(int, input().split())

table = []
queue = []
for i in range(N):
    temp = list(map(int, input().split()))
    table.append(temp)
    queue += [(i, j, v) for j, v in enumerate(temp) if v != 0]
    
S, X, Y = map(int, input().split())


queue.sort(key=lambda x:-x[2])

def start(queue):
    new_queue = queue[:]
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i, j, v in queue:
        visited[i][j] = True
    
    while queue:
        i, j, v = queue.pop()
        
        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ny, nx = dy + i, dx + j
            if N > ny >=0 and N > nx >=0 and table[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                new_queue.append((ny, nx, v))
                
    for y, x, cost in new_queue:
        table[y][x] = cost
    
    return sorted(new_queue + queue, key=lambda x:-x[2])

time = 0
while S > time:
    queue = start(queue)
    time += 1
    if table[X-1][Y-1] != 0:
        break
    
print(table[X-1][Y-1])

    
