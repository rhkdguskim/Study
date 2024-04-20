# https://www.acmicpc.net/problem/1987
import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

table = [ list(str(input())) for _ in range(R)]


temp = set()
temp.add(table[0][0])
queue = deque([(0, 0, temp)])

ans = 0

while queue:
    y, x, visited = queue.popleft()
    
    ans = max(ans, len(visited))
    
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny, nx = dy + y, dx + x
        if R > ny >=0 and C > nx >=0 and table[ny][nx] not in visited:
            new_visited = deepcopy(visited)
            new_visited.add(table[ny][nx])
            queue.append((ny, nx, new_visited))
            
print(ans)