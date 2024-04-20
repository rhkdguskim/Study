# https://www.acmicpc.net/problem/9328
import sys
from collections import deque

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
input = sys.stdin.readline

def init():
    global cost
    start_queue = []
    for i in range(h):
        if graph[i][0] == '.':
            start_queue.append((i, 0))
        elif graph[i][0] == '$':
            graph[i][0] = '.'
            cost += 1
            start_queue.append((i, 0))
        elif graph[i][0] == '*':
            pass
        elif graph[i][0].islower():
                key.add(graph[i][0])
                graph[i][0] = '.'
                start_queue.append((i, 0))
        else:
            if graph[i][0].lower() in key:
                graph[i][0] = '.'
                start_queue.append((i, 0))
            else:
                start_queue.append((i, 0))

        if graph[i][w-1] =='.':
            start_queue.append((i, w-1))
        elif graph[i][w-1] == '$':
            graph[i][w-1] = '.'
            cost += 1
            start_queue.append((i, w-1))
        elif graph[i][w-1] == '*':
            pass
        elif graph[i][w-1].islower():
            key.add(graph[i][w-1])
            graph[i][w-1] = '.'
            start_queue.append((i, w-1))
        else:
            if graph[i][w-1].lower() in key:
                graph[i][w-1] = '.'
                start_queue.append((i, w-1))
            else:
                start_queue.append((i, w-1))
                
    for i in range(1, w-1):
        if graph[0][i] == '.':
            start_queue.append((0, i))
        elif graph[0][i] == '$':
            graph[0][i] = '.'
            cost += 1
            start_queue.append((0, i))
        elif graph[0][i] == '*':
            pass
        elif graph[0][i].islower():
            key.add(graph[0][i])
            graph[0][i] = '.'
            start_queue.append((0, i))
        else:
            if graph[0][i].lower() in key:
                graph[0][i] = '.'
                start_queue.append((0, i))
            else:
                start_queue.append((0, i))
            
        if graph[h-1][i] == '.':
            start_queue.append((h-1, i))
        elif graph[h-1][i] == '$':
            cost += 1
            graph[h-1][i] = '.'
            start_queue.append((h-1, i))
        elif graph[h-1][i] == '*':
            pass
        elif graph[h-1][i].islower():
            key.add(graph[h-1][i])
            graph[h-1][i] = '.'
            start_queue.append((h-1, i))
        else:
            if graph[h-1][i].lower() in key:
                graph[h-1][i] = '.'
                start_queue.append((h-1, i))
            else:
                start_queue.append((h-1, i))
            
    return start_queue

def go(start_queue):
    global cost
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque()
    found_key = False
    
    for y, x in start_queue:
        visited[y][x] = True
        if graph[y][x] != '.':
            if graph[y][x].lower() in key:
                graph[y][x] = '.'
                queue.append((y, x))
                found_key = True
        else:    
            queue.append((y, x))

    
    while queue:
        y, x = queue.popleft()
        
        for dy, dx in moves:
            ny, nx = dy + y, dx + x
            if h > ny >=0 and w > nx >=0:
                if graph[ny][nx] != '*' and not visited[ny][nx]:
                    visited[ny][nx] = True
                    
                    if graph[ny][nx] == '.':
                        queue.append((ny, nx))
                        continue
                    
                    if graph[ny][nx] == '$':
                        graph[ny][nx] = '.'
                        cost += 1
                        queue.append((ny, nx))
                        continue
                    
                    if graph[ny][nx].isupper():
                        if graph[ny][nx].lower() in key:
                            graph[ny][nx] = '.'
                            queue.append((ny, nx))
                    else:
                        found_key = True
                        key.add((graph[ny][nx]))
                        graph[ny][nx] = '.'
                        queue.append((ny, nx))
    
    return found_key
                        
                        
                    
        

T = int(input())
result = []
for _ in range(T):
    h, w = map(int, input().split())
    graph = [list(str(input().strip())) for _ in range(h)]
    key = set()
    
    temp = str(input().strip())
    if temp[0] != '0':
        for c in temp:
            key.add(c)
            
    cost = 0
    start_queue = init()
    
    while True:
        found_key = go(start_queue)
    
        if not found_key:
            break
    result.append(cost)
    
for a in result:
    print(a)
    