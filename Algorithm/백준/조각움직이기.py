# https://www.acmicpc.net/problem/1035
# 한 별의 기준으로, 모든 별을 다 모아본다.

# 1. BFS 탐색으로 도착지의 후보를 만든다.
# 2. 하나의 도착지로 모은다. ( 도착지가 5개인경우 5개 모두 해본다.
    # 1. 각각의 도착지로 별을 하나씩 이동해보면서, 도착지 주변에 도착하면 하나의 별 탐색 끝.
    # 2. 도착지 주변을 갱신한다.
# 3. 가장 작은 이동거리를 계산한다.


# 1. 모든경우의수를 구한뒤, 연결되어 있는 경우만 필터링한다.
# 2. 연결되어있는경우를 BFS 탐색으로 최소거리를 모두 탐색해본다.

import sys
from itertools import combinations
from itertools import permutations

from collections import deque

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
input = sys.stdin.readline
graph = list(input().strip() for _ in range(5))

empty = []
peice = []
for i in range(5):
    for j in range(5):
        empty.append((i, j))
        if graph[i][j] == '*':
            peice.append((i, j))
            

def check(i, j):
    return 5 > i >= 0 and 5 > j >=0
            
def bfs(i, j, group):
    queue = deque()
    queue.append((i, j))
    new_graph = [['.' for _ in range(5)] for _ in range(5)]
    for g_y, g_x in group:
        new_graph[g_y][g_x] = '*'
        
    new_group = []
    new_group.append((i, j))
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[i][j] = True
    while queue:
        y, x = queue.popleft()
        for dy, dx in moves:
            ny, nx  = dy + y, dx + x
            if check(ny, nx) and not visited[ny][nx] and new_graph[ny][nx] == '*':
                visited[ny][nx] = True
                queue.append((ny, nx))
                new_group.append((ny, nx))
                
    return len(new_group) == len(group)

def isGroup(i, j, group):
    return bfs(i, j, group)


groups = list(combinations(empty, len(peice)))
groups = [new_g for new_g in groups if isGroup(new_g[0][0], new_g[0][1], new_g)]

def checkdif(source, target):
    return abs(source[0] - target[0]) + abs(source[1] - target[1])

ans = 10000

peice.sort()

for group in groups:
    for p_group in list(permutations(group, len(peice))):
        cost = 0
        for i in range(len(peice)):
            cost += checkdif(peice[i], p_group[i])    
            
        ans = min(cost, ans)
    
print(ans)