# https://www.acmicpc.net/problem/2638
# 1. 너비우선탐색 접근법
# - (0,0) 부터 탐색하여 외부공기, 내부공기를 분리한다.
# - 녹는 치즈를 계산하고 일수를 높힌다.
# 치즈가 없어질때까지 무한반복

# 2. 깊이우선탐색 접근법
# - (0,0)부터 탐색한다. 치즈를 찾는다. (치즈를 찾는과정에서 가중치를 찾는데 내부공기는 -1를 외부공기는 1을 return 한다.)
# 외부공기는 외부공기로 초기화된 그래프를 만나면 외부공기이다, 내부공기는 다 탐색해보았는데 외부공기와 만나지 못하면 내부공기이다.
from pprint import pprint
import sys
sys.setrecursionlimit(200000)
move = ((0,1), (0,-1), (1,0), (-1,0))
N, M = map(int, input().split()) # 세로, 가로
graph = []
for _ in range(N):
    arr = list(map(int ,input().split()))
    graph.append(arr)
    
def dfs(i,j, searchArea):
    searchArea[i][j] = 1
    for dy, dx in move:
        ny = dy + i
        nx = dx + j
        if N > ny >=0 and M > nx >=0:
            if graph[ny][nx] == 1: # 치즈이면
                searchArea[ny][nx] += 1
            else: # 외부공기이면
                if searchArea[ny][nx] == 0:
                    dfs(ny,nx, searchArea)
                
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
    dfs(0,0, searchArea)
                        
    for i in range(N):
        for j in range(M):
            if searchArea[i][j] >= 2: # 외부공기 가중치가 2보다 클경우 없앤다.
                graph[i][j] = 0
                
print(time)