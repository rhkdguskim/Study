# https://www.acmicpc.net/problem/2636
move = [(0,1), (1,0), (0,-1), (-1,0)]
from collections import deque
H,W = map(int, input().split())
table = []

for _ in range(H):
    table.append(list(map(int, input().split())))
def meltcheeze():
    visited = [[False for _ in range(W)] for _ in range(H)] # bfs 방문처리
    cnt = 0 # 녹을 치즈 개수를 샌다.
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True
    while queue:
        i,j = queue.popleft()
        for dy,dx in move:
            ny = dy + i
            nx = dx + j
            if H > ny >= 0 and W > nx >= 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                if table[ny][nx] == 0: # 치즈가 아닐때문 이어서 방문
                    queue.append((ny,nx))

    for i in range(H):
        for j in range(W):
            if table[i][j] and visited[i][j]: # 치즈를 녹인다.
                cnt += 1
                table[i][j] = 0

    return cnt

time = 0
ans = 0
prev = 0
while True:
    ans = meltcheeze()
    if ans == 0:
        break

    time+=1
    prev = ans

print(time)
print(prev)





