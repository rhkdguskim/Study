from collections import deque
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(str, input())))

queue = deque()
visited = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]

def appendQueue(i, j, str, visited):
    if(N > i >= 0 and N > j >= 0): # i,j가 정상범위 안에 있는지 체크
        if (not visited[i][j]) and (arr[i][j] == str): # str값이 일치하고 방문하지 않았다면 큐에 추가
            queue.append([i,j])
            visited[i][j] = True
            
def bfs(i,j, str, visited):
    if (not visited[i][j]) and (arr[i][j] == str): # str값이 일치하고 방문하지 않았다면 큐에 추가
        queue.append([i,j])
        visited[i][j] = True
    else:
        return False
    while queue:
        y,x = queue.popleft()
        appendQueue(y-1, x, str, visited)
        appendQueue(y+1, x, str, visited)
        appendQueue(y, x-1, str, visited)
        appendQueue(y, x+1, str, visited)
    
    return True # 방문이 완료되면 True값을 Return 한다.

count = 0
count2 = 0
for i in range(N):
    for j in range(N):
        if(bfs(i,j,"R", visited)):
            count += 1
        elif(bfs(i,j,"G", visited)):
            count += 1
        elif(bfs(i,j,"B", visited)):
            count += 1 
            
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if(bfs(i,j,"R", visited2)):
            count2 += 1
        elif(bfs(i,j,"G", visited2)):
            count2 += 1
        elif(bfs(i,j,"B", visited2)):
            count2 += 1 
            
print(count, count2)