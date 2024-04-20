from collections import deque
INF = int(10e9)
N, K = map(int, input().split())
arrlen = 0
if(N > K):
    arrlen = N+1
else :
    arrlen = K+1

visited = [INF] * arrlen
def findsubin(subin):
    queue = deque()
    queue.append([subin, 0])
    
    while queue:
        now, time = queue.popleft()
        if(0<= now < arrlen and visited[now] > time):
            visited[now] = time
            # x - 1
            queue.append([now-1, visited[now]+1])
            # x + 1
            queue.append([now+1, visited[now]+1])
            # x * 2
            queue.append([now*2, visited[now]])
            
findsubin(N)
print(visited)