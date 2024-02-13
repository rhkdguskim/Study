# https://www.acmicpc.net/problem/13913
from collections import deque
from copy import deepcopy
N, K = map(int, input().split()) # 수빈이의 위치, 동새의 위치
graph = [False for _ in range(100001)]
queue = deque()

visitedqueue = [N]
graph[N] = True
queue.append((N, 0, visitedqueue)) # 자기자신은 0초로 초기화한다

while queue:
    X, time, visitedqueue = queue.popleft()
    
    if X == K:
        print(time)
        print(*visitedqueue)
        break
    
    # 2X로 이동(순간이동)
    moveType3 = X*2
    if 100000 >= moveType3 >= 0 and not graph[moveType3]:
        graph[moveType3] = True
        queue.append((moveType3, time + 1, deepcopy(visitedqueue) + [moveType3]))
    
    # X-1로 이동
    moveType1 = X - 1
    if 100000 >= moveType1 >= 0 and not graph[moveType1]:
        graph[moveType1] = True
        queue.append((moveType1, time + 1, deepcopy(visitedqueue) + [moveType1] ))
    
    # X+1로 이동
    moveType2 = X + 1
    if 100000 >= moveType2 >= 0 and not graph[moveType2]:
        graph[moveType2] = True
        queue.append((moveType2, time + 1 , deepcopy(visitedqueue) + [moveType2]))
    