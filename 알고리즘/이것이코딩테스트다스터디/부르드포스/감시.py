# https://www.acmicpc.net/problem/15683
# CCTV를 하나씩 돌려보면서 최소사각지대 감시구역 테이블을 구한다.
# 깊이우선탐색 그래프 탐색, 재귀 호출로 N개의 cctv를 방문기록하며 최소값을 갱신

import copy
cctv = ['1','2','3','4','5']
N, M = map(int, input().split()) # N은 세로크기, M은 가로크기
graph = []
cctvlist = []
for i in range(N):
    table = list(map(str, input().split()))
    for j in range(M):
        if table[j] in cctv:
            cctvlist.append((i,j))
    graph.append(table)

def getBilndArea(table): # 현재 테이블에서 사각지대를 구한다.
    counter = 0
    for i in range(N):
        for j in range(M):
            if table[i][j]  == '0':
                counter += 1
    return counter

def dfs(i,j, move, table):
    ny = i + move[0]
    nx = j + move[1]
    if N > ny >=0 and M > nx >=0 and table[ny][nx] != '6':
        table[ny][nx] = '#'
        dfs(ny,nx, move, table)

move = [[],
        [[(0,1)],[(0,-1)], [(1,0)], [(-1,0)]],  #1번
        [[(1,0), (-1,0)], [(0,1), (0,-1)]], # 2번
        [[(-1,0), (0,1)], [(0,1), (1,0)], [(1,0), (0,-1)], [(-1,0), (0,-1)]], # 3번
        [[(0,-1), (0,1), (-1,0)], [(1,0), (0,1), (-1,0)], [(1,0), (0,1), (0,-1)], [(1,0), (-1,0), (0,-1)]],  # 4번
        [[(0,1), (1,0), (-1,0), (0,-1)]]] # 5번

minvalue = int(10e9)
def cctv(table, depth):
    global minvalue
    if depth == len(cctvlist): # 모두 방문 했으므로 사각지대를 샌다.
        minvalue = min(minvalue, (getBilndArea(table)))
        return

    i,j = cctvlist[depth];
    for moves in move[int(graph[i][j])]: # 각 cctv를 돌려본다.
        temp = copy.deepcopy(table)
        for m in moves:
            dfs(i,j,m, temp)
            
        cctv(temp, depth + 1)

cctv(graph, 0)
print(minvalue)