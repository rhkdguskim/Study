# https://www.acmicpc.net/problem/7576

M, N = map(int, input().split())

table = []
for _ in range(N):
    table.append(list(map(int,input().split())))
    
visited = [[False for _ in range(M)] for _ in range(N)]

def addQueue(queue, i,j):
    if M > j >= 0 and N > i >= 0 :
        if table[i][j] != -1 and visited[i][j] == False: # 익지 않는 토미토는 방문하지 않는다.
            visited[i][j] = True
            queue.append([table[i][j], i, j])


def initQueue(queue): # 익은 토마토로부터 시작
    for i in range(N):
        for j in range(M):
            if table[i][j] != -1:
                return addQueue(queue, i,j)

bfsqueue = []
initQueue(bfsqueue)

counter = 0
while bfsqueue:
    tomato, i, j = bfsqueue.pop()
    addQueue(bfsqueue, i+1,j)
    addQueue(bfsqueue, i-1,j)
    addQueue(bfsqueue, i,j+1)
    addQueue(bfsqueue, i,j-1)
    
print(visited)
print(table)
