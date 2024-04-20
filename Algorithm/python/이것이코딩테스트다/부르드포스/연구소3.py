# https://www.acmicpc.net/problem/17142
# 0은 빈칸 1은벽 2는 바이러스의 위치
# 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다. (활성바이러스0, 비활성바이러스 *)
# 너비우선탐색으로 시간값을 초기화하며 방문한다(이미 방문한 친구는 값을 확인해보아 최소값이 될경우 다시 재방문하여 최소값으로 만들어준다.)
# M개의 활성바이러스를 선택하였을때 최소값을 구하라 ( 조합 문제 ) 모든 조합의 경우를 완전탐색으로 문제를 해결한다.
from collections import deque
from itertools import combinations
from copy import deepcopy
N ,M = map(int, input().split()) # N은 가로세로의 크기, M은 비활성 바이러스의 개수
INF = int(10e9)
graph = list()
viruslist = list()
move = [(0,1), (0,-1), (1,0), (-1,0) ]
for i in range(N):
    table = list(map(int ,input().split()))
    graph.append(table)
    for j in range(N):
        if table[j] == 0: # 빈칸일경우(바이러스가 감염 될 수 있음)
            graph[i][j] = 0
        elif table[j] == 1: # 벽일경우
            graph[i][j] = '-'
        else : # 비활성바이러스일경우
            graph[i][j] = '*'
            viruslist.append([i,j])
            
def Virus(virus):
    queue = deque()
    table = deepcopy(graph)
    for vir in virus:
        queue.append((vir[0], vir[1], 0)) # 활성바이러스를 넣는다.
    maxcost = 0
    while queue:
        y,x, cost = queue.popleft()
        for dy, dx in move:
            ny = dy + y
            nx = dx + x
            if N > ny >=0 and N > nx >=0 and (table[ny][nx] == 0 or table[ny][nx] == '*'): # 빈칸일 경우 혹은 비활성바이러스(퍼뜨려야하기때문)일 경우만 방문한다.
                queue.append((ny, nx, cost + 1))
                if table[ny][nx] == 0: # 비활성바이러스는 최대값에 관여하지 않는다.
                    maxcost = max(maxcost, cost + 1)
                table[ny][nx] = cost + 1


    # 모두 다 방문했을 경우만 결과값으로 리턴하고 그렇지 않다면 -1을 리턴한다.
    for i in range(N):
        for j in range(N):
            if table[i][j] == 0:
                return -1
    
    return maxcost
                    
mincost = INF
for virus in combinations(viruslist, M):
    cost = Virus(virus)
    if cost != -1: # 다 방문했을때만 최소값을 초기화 한다.
        mincost = min(mincost, cost)

if mincost == INF: # 모두 다 방문했지만 전부 퍼트리지 못한경우
    print(-1)
else:
    print(mincost)