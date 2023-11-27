# https://www.acmicpc.net/problem/8982
import sys
input = sys.stdin.readline

N = int(input())
edge = []
max_y = 0
max_x = 0
for _ in range(N):
    a, b = map(int, input().split())
    edge.append((a, b)) # 가로, 세로
    max_x = max(a, max_x)
    max_y = max(b, max_y)
    
K = int(input())
hole = []
for _ in range(K):
    a, b, c, d = map(int, input().split())
    hole.append((a, b, c, d)) # 가로, 세로, 가로, 세로
    
graph = [[False for _ in range(max_x)] for _ in range(max_y)]

# 2개씩 짝이므로 물을 채워나간다.
for i in range(1, N-1, 2):
    x1, y1 = edge[i]
    x2, y2 = edge[i+1]
    for i in range(y1):
        for j in range(x1, x2):
            graph[i][j] = True

# 물을 빼낸다.
for x1, y1, x2, y2 in hole:
    left_idx = edge.index((x1, y1))
    right_idx = edge.index((x2, y2))
    
    left_y = y1
    right_y = y2
    left_x = x1
    right_x = x2
    while left_idx > 0:
        left_idx -= 1
        if edge[left_idx][1] < y1:
            left_x = edge[left_idx][0]
            left_y = edge[left_idx][1]
            break
    
    while N > right_idx:
        right_idx += 1
        if edge[right_idx][1] < y2:
            right_x = edge[right_idx][0]
            right_y = edge[right_idx][1]
            break
    
    for i in range(y1):
        for j in range(left_x, right_x):
            graph[i][j] = False
            
    for i in range(left_y):
        for j in range(left_x):
            graph[i][j] = False
    
    for i in range(right_y):
        for j in range(max_x-1, right_x-1, -1):
            graph[i][j] = False
    
ans = 0
for i in range(max_y):
    for j in range(max_x):
        if graph[i][j] == True:
            ans += 1

# for g in graph:
#     print(g)  
print(ans)