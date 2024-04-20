#https://www.acmicpc.net/problem/13460
# 1. 빨간색을 기준으로 벽이 없는곳을 기울이기 동작을 해본다.
# 2. 빨간색이 기울이기 동작을 하는도중 파란색을 만나면 파란색을 먼저 기울인다.
# 2.1 파란색이 갈 수 없는경우 탐색을 종료한다.
# 2.2 파란색이 다 기울어지면(한번이라도 움직이면) 빨간색을 마저 기울인다.
# 3. 기울이기 카운트를 증가한다.
# 4. 빨간색이 구슬을 만나면 종료한다, 그렇지 않으면 다시 1번으로 간다. ( 기울이기 카운트 증가)
from collections import deque
movetype = [(1,0), (-1,0), (0,1), (0,-1)] # 아래, 위로, 우측, 좌측
N, M = map(int, input().split()) # 세로, 가로

board = []
red = [0,0]
for i in range(N):
    newtable = list(str(input()))
    for j in range(M):
        if newtable[j] == 'R':
            red[0] = i
            red[1] = j
    board.append(newtable)

print(red)

def dfs(i,j,color,type):
    # 움직이는 타입에 타라서 깊이우선탐색
    ny = i + movetype[type][0]
    nx = j + movetype[type][1]
    if N > ny >=0 and M > nx >=0:
        if board[ny][nx] == '.': # 빈칸이라면 다음 칸으로 탐색
            board[ny][nx] = color
            dfs(ny,nx,color, type)
            return True
        elif board[ny][nx] == '#': # 벽이 있다면 다음칸으로 탐색 불가
            return False
        elif color == 'R' and board[ny][nx] == 'B': # 빨간색이 파란색을 만났을때 파란색을 먼저 이동시킨후 다시 탐색
            if dfs(ny,nx,'B', type): # 파란색이 탐색을 할 수 있다면
                dfs(i,j, color, type) # 다시 탐색 시작
            else:
                return False
        elif color == 'B' and board[ny][nx] == 'R': # 파란색이이 빨간색을 만났을때 빨간색을 먼저 이동시킨후 다시 탐색
            if dfs(ny,nx,'R', type): # 빨간색이 탐색을 할 수 있다면
                dfs(i,j, color, type) # 다시 탐색 시작
            else:
                return False
        else : # 목적지에 도달하였다면
            return True
        
    else:
        return False
    
def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    
    for k in range(4):
        