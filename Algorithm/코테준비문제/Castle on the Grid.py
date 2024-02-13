# https://www.hackerrank.com/challenges/castle-on-the-grid/problem?isFullScreen=true
# 너비우선탐색으로 탐색한다.
# move움직임이 이전과 반대방향으로 바뀌었다면 cost값을 1 증가시킨다.
'''
3
.X.
.X.
...
0 0 0 2
'''

import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
move = [(0,1), (0,-1), (1,0), (-1,0)]

n = int(input())
graph = []
for _ in range(n):
    graph.append(str(input()))

s_x, s_y, e_x, e_y = map(int, input().split())

queue = deque()
new = set()
new.add((s_x, s_y))
queue.append((s_x, s_y, -1, 1, new))
ans = 100 * 100 + 1
while queue:
    y, x, dir, cost, visit = queue.popleft()
    for t in range(4):
        dy, dx = move[t]
        ny, nx = y+dy, x+dx
        if n > ny >= 0 and n > nx >=0 and graph[ny][nx] == '.' and (ny, nx) not in visit:
            if cost > ans:
                continue

            if dir != -1 and dir != t:
                cost += 1
            if ny == e_x and nx == e_y:
                print(visit)
                ans = min(cost, ans)

            newvisit = deepcopy(visit)
            newvisit.add((ny, nx))
            queue.append((ny, nx, t, cost, newvisit))

if s_x == e_x and s_y == e_y:
    print(0)
else:
    print(ans)