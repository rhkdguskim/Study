# https://www.acmicpc.net/problem/2251
import sys
from collections import deque
input = sys.stdin.readline

a, b, c = map(int, input().split())

visited = [[False] * 201 for _ in range(201)]
result = set()

def bfs():
    queue = deque()
    queue.append((0, 0, c))
    result.add(c)
    while queue:
        x, y, z = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        if x == 0:
            result.add(z)
        if x + y > b:
            queue.append((x + y - b, b, z))
        else:
            queue.append((0, x + y, z))
        if x + z > c:
            queue.append((x + z - c, y, c))
        else:
            queue.append((0, y, x + z))
        if y + x > a:
            queue.append((a, y + x - a, z))
        else:
            queue.append((x + y, 0, z))
        if y + z > c:
            queue.append((x, y + z - c, c))
        else:
            queue.append((x, 0, y + z))
        if z + x > a:
            queue.append((a, y, z + x - a))
        else:
            queue.append((z + x, y, 0))
        if z + y > b:
            queue.append((x, b, z + y - b))
        else:
            queue.append((x, z + y, 0))
            
bfs()
result = list(result)
result.sort()
print(' '.join(map(str, result)))