# https://www.acmicpc.net/problem/2252
from collections import deque
N , M = map(int, input().split())
table =  [0 for _ in range(N)]
graph = [[] for _ in range(N)]
for _ in range(M):
    A,B = map(int ,input().split())
    graph[A-1].append(B)
    table[B-1] += 1 # 진입차수를 넣는다.
    
    
queue = deque()

for i in range(N):
    if table[i] == 0:
        queue.append(i+1) # 진입차수가 0인 수를 큐에 넣는다.
        

while queue:
    num = queue.popleft()
    print(num, end=' ')
    
    for newnum in graph[num-1]:
        table[newnum-1] -= 1
        
        if table[newnum-1] == 0: # 진입차수가 0이되면 큐에 넣는다.
            queue.append(newnum)
            
