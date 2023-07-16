# https://www.acmicpc.net/problem/3190
from collections import deque
N = int(input()) # 보드의 크기
board = [[0 for _ in range(N)] for _ in range(N)]
K = int(input()) # 사과 개수
movetypes = ['E','S','W','N'] # 동쪽, 남쪽, 서쪽, 북쪽 을 뱀이 보고있는상태
move = [[0,1], [1,0], [0,-1], [-1,0]] # 동,남,서,북을 움직인다.
for _ in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1 # 사과의 위치를 저장한다.

snakemove = []
L = int(input()) # 뱀의 위치 변환 횟수
for _ in range(L):
    sec, movetype = map(str, input().split())
    snakemove.append([int(sec), movetype])

def turnLeft(status):
    idx = movetypes.index(status)
    if idx - 1 < 0:
        return movetypes[-1]
    else:
        return movetypes[idx-1]
    
def turnRight(status):
    idx = movetypes.index(status)
    if idx+1 == 4:
        return movetypes[0]
    else:
        return movetypes[idx+1]

snakequeue = deque()
queue = deque()
queue.append([0,0, 'E'])
time = 0

while queue:
    i, j, snakestatus = queue.popleft()
    snakequeue.append([i,j]) # 뱀의 머리를 늘려 위치시킨다.
    for sec, type in snakemove:
        if sec == time:
            if type == 'L': #왼쪽으로 방향전환
                snakestatus = turnLeft(snakestatus)
            else: # 오른쪽으로 방향전환
                snakestatus = turnRight(snakestatus)
    idx = movetypes.index(snakestatus)
    dy = i + move[idx][0]
    dx = j + move[idx][1]
    time += 1
    if N > dy >= 0 and N > dx >=0: # 벽
        if [dy,dx] not in snakequeue: # 자신의 몸이랑 부딛힘
            queue.append([dy,dx, snakestatus])
            if board[dy][dx] != 1: # 사과가 없으면 꼬리를 삭제한다.
                snakequeue.popleft()
            else :
                board[dy][dx] = 0
                
print(time)