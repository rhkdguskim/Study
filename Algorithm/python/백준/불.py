# https://www.acmicpc.net/problem/4179
# 너비우선탐색문제.

import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())

table = []
queue = deque()
ji_hun = []
for i in range(R):
    temp = list(str(input().strip()))
    for j in range(C):
        if temp[j] == "F":
            queue.append((i, j, 'F', 0))
        elif temp[j] == "J":
            ji_hun.append((i, j, 'J', 0))
            
    table.append(temp)
    
def is_end(y, x):
    return 0 == y or y == R-1 or 0 == x or x == C-1

is_arrived = False

for hun in ji_hun:
    queue.append(hun)
    
while queue:
    y, x, what, cost = queue.popleft()
    
    if what == 'J' and is_end(y, x):
        print(cost + 1)
        is_arrived = True
        break

    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny, nx = dy + y, dx + x
        if R > ny >=0 and C > nx >=0 and table[ny][nx] == '.':
            table[ny][nx] = what
            queue.append((ny, nx, what, cost + 1))

if not is_arrived:
    print("IMPOSSIBLE")