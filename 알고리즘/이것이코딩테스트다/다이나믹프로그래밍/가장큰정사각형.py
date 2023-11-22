# https://www.acmicpc.net/problem/1915
from pprint import pprint
n, m = map(int, input().split())
move = [(-1,-1), (-1,0), (0,-1)]
cost = [-1 for _ in range(3)]
graph = [[] for _ in range(n)]
for i in range(n):
    char = list(str(input()))
    for num in char:
        graph[i].append(int(num))
        

maxresult = 0
for i in range(n):
    for j in range(m):
        
        for t in range(len(cost)): # 초기값 Init
            cost[t] = -1
        
        for k in range(len(move)):
            dy = i + move[k][0]
            dx = j + move[k][1] 
            if n > dy >= 0 and m > dx >= 0 and graph[dy][dx]:
                cost[k] = graph[dy][dx] + 1
                
        comp = min(cost)
        
        if graph[i][j]:
            graph[i][j] = max(comp, graph[i][j])
            maxresult = max(maxresult, graph[i][j])

print(maxresult*maxresult)