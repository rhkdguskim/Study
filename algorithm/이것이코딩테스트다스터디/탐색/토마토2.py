# https://www.acmicpc.net/problem/7569
from collections import deque
M,N,H = map(int, input().split()) # 가로, 세로, 높이

graph = [[] for _ in range(H)]
visited = [[[False for _ in range(M)] for _ in range(N)] for _ in range(H)]
nonrapedtomato = 0
rapedtomato = []
for i in range(H): # 총 토마토 박수 개수
    for j in range(N): # 세로의 크기
        arr = list(map(int, input().split()))
        for k in range(M):
            if arr[k] == -1:
                visited[i][j][k] = True
            elif arr[k] == 0:
                nonrapedtomato += 1 
            elif arr[k] == 1:
                rapedtomato.append([i, j, k, 0])
                
        graph[i].append(arr)

queue = deque()
for tomato in rapedtomato:
    queue.append(tomato)

tomatocounter = 0
maxday = 0
while queue: # i 는 높이, j는 세로, k는 가로
    i,j,k,day = queue.popleft()
    if H > i >=0 and N > j >=0 and M > k >=0 and not visited[i][j][k]:
        if graph[i][j][k] == 0:
            tomatocounter += 1
        maxday = max(maxday, day)
        visited[i][j][k] = True
        queue.append([i+1,j,k, day + 1]) # 위
        queue.append([i-1,j,k, day + 1]) # 아래
        queue.append([i,j+1,k, day + 1]) # 세로아래
        queue.append([i,j-1,k, day + 1]) # 세로위
        queue.append([i,j,k+1, day + 1]) # 가로오른
        queue.append([i,j,k-1, day + 1]) # 가로왼

if nonrapedtomato == 0:
    print(0)
else:
    if nonrapedtomato != tomatocounter:
        print(-1)
    else:
        print(maxday)