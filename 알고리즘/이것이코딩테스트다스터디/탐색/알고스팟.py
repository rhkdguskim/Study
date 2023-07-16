# https://www.acmicpc.net/problem/1261
from collections import deque
INF = int(10e9)
M, N = map(int, input().split()) # M 가로의 크기, N 세로의 크기
table = []
dp = [[INF for _ in range(M)] for _ in range(N)] # 최단경로를 저장하기위한 dp 테이블

for i in range(N): # 세로의 길이만큼 배열추가
    table.append(list(map(int, input())))
    
def appendQueue(queue, i,j, wallbreak):
    if(M > j >=0 and N > i >= 0):
        if dp[i][j] > wallbreak: # dp 테이블을 갱신한다. 현재 dp테이블보다 클경우 탐색을 멈춘다.
            dp[i][j] = wallbreak
            if table[i][j] == 1: # 벽이 있다면
                queue.append([i,j,wallbreak+1]) # 벽을 부수고 들어간다 가중치 +1
            else :
                queue.append([i,j,wallbreak]) # 벽이 없으면 그냥 이동한다.

def bfs(i,j):
    queue = deque() # 큐 자료구조
    appendQueue(queue, i,j, 0)

    while queue:
        i,j, wallbreak = queue.popleft()
            
        appendQueue(queue, i+1,j, wallbreak) # 하
        appendQueue(queue, i-1,j, wallbreak) # 상
        appendQueue(queue, i,j-1, wallbreak) # 좌
        appendQueue(queue, i,j+1, wallbreak) # 우
    
bfs(0, 0) # 0,0 으로 너비우선 탐색한다.
print(dp[N-1][M-1]) # 최종 목적지를 출력한다.