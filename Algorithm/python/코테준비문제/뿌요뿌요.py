# https://www.acmicpc.net/problem/11559
# 1. 모양이 있는지 확인한다.
# 2. 모양이 있는 애들은 다 부순다.
# 3. 중력에 의해 다 떨어진다.
# 4. 1~3번을 반복한다. 모양이 없으면 종료한다.
from pprint import pprint
from collections import deque
N, M = 12, 6  # 높이가 12 가로가 6

shape = ((0, 1), (1, 0), (-1, 0), (0, -1))  # ㅗ, ㅜ, ㅏ, ㅓ
speicalshape = ((1, 0), (0, 1), (1, 1))  # 사각형 모양

graph = []

for _ in range(N):
    graph.append(list(map(str, input())))

def checkshpae2(i,j, color):
    queue = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[i][j] = True
    queue.append((i, j, 1))
    while queue:
        y, x, cost = queue.popleft()
        if cost == 4: # ㅡ, ㅣ ... 모양
            return True

        for dy, dx in shape:
            ny, nx = dy + y, dx + x
            if N > ny >=0 and M > nx >=0 and not visited[ny][nx]:
                visited[ny][nx] = True
                if graph[ny][nx] == color:
                    queue.append((ny, nx, cost + 1))

    return False

def checkshape(i, j, color):
    cnt = 0
    for dy, dx in shape:
        ny, nx = dy + i, dx + j
        if N > ny >= 0 and M > nx >= 0:
            if graph[ny][nx] == color:
                cnt += 1

    if cnt >= 3:
        return True
    else:
        return False

def checkspiecalshape(i,j, color):
    cnt = 0
    for dy, dx in speicalshape:
        ny, nx = dy +i, dx +j
        if N > ny >= 0 and M > nx >= 0:
            if graph[ny][nx] == color:
                cnt += 1

    if cnt == 3:
        return True
    else:
        return False

def puyopuyo(i, j, color):
    queue = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[i][j] = True
    queue.append((i,j))
    while queue:
        y, x = queue.popleft()
        graph[y][x] = '.'
        for dy, dx in shape:
            ny, nx = dy + y, dx + x
            if N > ny >=0 and M > nx >=0 and not visited[ny][nx]:
                visited[ny][nx] = True
                if graph[ny][nx] == color:
                    queue.append((ny, nx))

    return
def gravity():
    for i in range(M): # x좌표
        queue = deque()
        for j in range(N-1, -1, -1): # 아래서 부터 보면서 순차 큐에 넣는다.
            if graph[j][i] != '.':
                queue.append(graph[j][i])

        idx = N-1
        for t in queue: # Queue 에 있는값을 아래서부터 채운다.
            graph[idx][i] = t
            idx -= 1

        for t in range(idx, -1, -1): # 나머지부분은 빈칸으로 만들어준다.
            graph[t][i] = '.'



ans = 0
while True:
    cnt = 0
    for i in range(N):
        for j in range(M):
            #print(graph[i][j])
            if graph[i][j] != '.' and (checkshape(i,j, graph[i][j]) or checkspiecalshape(i,j, graph[i][j])or checkshpae2(i,j, graph[i][j])): # 모양의 조건이 맞다면
                puyopuyo(i,j, graph[i][j]) # 푸요푸요 한다.
                cnt += 1

    if cnt == 0: # 푸요푸요 할 것이 없다면 종료
        break

    gravity()
    #pprint(graph)
    ans += 1

print(ans)