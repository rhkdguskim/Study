#https://www.acmicpc.net/problem/2623
from collections import deque


N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
in_drgree = [0 for _ in range(N+1)]
for _ in range(M):
    arr = list(map(int, input().split()))
    
    for i in range(1, len(arr)-1):
        graph[arr[i]].append(arr[i+1])
        in_drgree[arr[i+1]] += 1
        
queue = deque()
resultqueue = []
for i in range(1, N+1):
    if in_drgree[i] == 0:
        queue.append(i)
    
while queue:
    num = queue.popleft()
    resultqueue.append(num)
    
    for newnum in graph[num]:
        in_drgree[newnum] -= 1
        if in_drgree[newnum] == 0:
            queue.append(newnum)
            
if len(resultqueue) == N:
    for num in resultqueue:
        print(num)
else:
    print(0)