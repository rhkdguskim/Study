import sys
from collections import deque

input = sys.stdin.readline
# BFS로 문제를 풀어보자
X = int(input())

visited = [False for _ in range(X+1)]

queue = deque()
queue.append((X, 0)) # X를 시작점으로하고 타깃이 1이다.
visited[X] = True

while queue:
    x, cost = queue.popleft()
    if x == 1:
        print(cost)
        break
    
    if x % 5 == 0 and not visited[x//5]: # X를 5로 나눌수 있다면 5로 나눈다.
        visited[x//5] = True
        queue.append((x//5, cost + 1))
        
    if x % 3 == 0 and not visited[x//3]: # X를 3으로 나눌수 있다면 3으로 나눈다.
        visited[x//3] = True
        queue.append((x//3, cost + 1))
        
    if x % 2 == 0 and not visited[x//2]: # X를 2으로 나눌수 있다면 2으로 나눈다.
        visited[x//2] = True
        queue.append((x//2, cost + 1))
        
    if x - 1 >= 1 and not visited[x-1]: # X를 2으로 나눌수 있다면 2으로 나눈다.
        visited[x-1] = True
        queue.append((x-1, cost + 1))
