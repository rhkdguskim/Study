# https://www.acmicpc.net/problem/7576

M, N = map(int, input().split())
table = []
for _ in range(N):
    table.append(list(map(int,input().split())))
    
visited = [[False for _ in range(M)] for _ in range(N)]

def addQueue(queue, i,j):
    if M > j >= 0 and N > i >= 0 and not visited[i][j]:
        visited[i][j] = True
        queue.append([i, j])

queue = []
for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            visited[i][j] = True
            queue.append([i,j])
        if table[i][j] == -1:
            visited[i][j] = True
            
counter = 0
while queue:
    stepqueue = []
    while queue:
        i, j = queue.pop()
        addQueue(stepqueue, i+1, j)
        addQueue(stepqueue, i-1, j)
        addQueue(stepqueue, i, j+1)
        addQueue(stepqueue, i, j-1)
    
    if not stepqueue:
        break
    
    counter +=1
    queue = stepqueue

notfinished = False
for i in range(N):
    for j in range(M):
            if visited[i][j] == False:
                notfinished = True
                break
    if notfinished:
        break

if notfinished:
    print(-1)
else:
    print(counter)
    