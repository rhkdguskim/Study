# https://www.acmicpc.net/problem/2638
# 1. 너비우선탐색 접근법
# - (0,0) 부터 탐색하여 외부공기, 내부공기를 분리한다.
# - 녹는 치즈를 계산하고 일수를 높힌다.
# 치즈가 없어질때까지 무한반복

from collections import deque
from pprint import pprint

move = ((0,1), (0,-1), (1,0), (-1,0))
N, M = map(int, input().split()) # 세로, 가로
graph = []
for _ in range(N):
    arr = list(map(int ,input().split()))
    graph.append(arr)


def bfs(i,j):
    queue = deque()
    searchArea[i][j] = 1
    queue.append((i,j))
    while queue:
        y,x = queue.popleft()
        for dy, dx in move:
            ny = dy + y
            nx = dx + x
            if N > ny >=0 and M > nx >=0:
                if graph[ny][nx] == 1: # 치즈이면
                    searchArea[ny][nx] += 1
                else: # 외부공기이면
                    if searchArea[ny][nx] == 0:
                        searchArea[ny][nx] = 1
                        queue.append((ny,nx))
                        
def getCheezeCount():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1: # 치즈가 하나라도 있으면 False 리턴
                return True
    
    return False

time = 0
while(getCheezeCount()): # 치즈가 다 녹아 없어질때까지
    time += 1
    searchArea = [[0 for _ in range(M)] for _ in range(N)] # 외부공기 가중치값 저장 배열
    bfs(0,0)     
    for i in range(N):
        for j in range(M):
            if searchArea[i][j] >= 2: # 외부공기 가중치가 2보다 클경우 없앤다.
                graph[i][j] = 0
    
print(time)